-- 1. Создаем базу данных и выбираем её
CREATE DATABASE IF NOT EXISTS hr_simple;
USE hr_simple;

-- 2. Создаем таблицу сотрудников
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,       -- ID сотрудника
    full_name VARCHAR(255) NOT NULL,         -- ФИО целиком (проще для начала)
    birth_date DATE NOT NULL,                -- Дата рождения (лучше, чем возраст)
    phone VARCHAR(20),                       -- Телефон
    email VARCHAR(100) UNIQUE,               -- Почта (уникальная)
    department VARCHAR(100) DEFAULT 'Общий', -- Отдел
    position VARCHAR(100) DEFAULT 'Сотрудник',-- Должность
    salary DECIMAL(10, 2) DEFAULT 0,         -- Зарплата (число с копейками)
    hire_date DATE DEFAULT (CURDATE()),      -- Дата приема на работу
    is_active BOOLEAN DEFAULT TRUE           -- Работает ли сейчас (TRUE/ FALSE)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Добавляем данные
INSERT INTO employees (full_name, birth_date, phone, email, department, position, salary) VALUES
('Иванов Иван Иванович', '1990-05-15', '+79991112233', 'ioan14@mail.ru', 'IT', 'Программист', 60000.00),
('Иванов Иван Иванович', '2003-09-03', '+79614584627', 'olya2003@mail.ru', 'IT', 'Системный администратор', 38000.00),
('Петрова Анна Сергеевна', '1995-08-22', '+79948956166', 'anna97@mail.ru', 'Бухгалтерия', 'Бухгалтер', 65000.00),
('Сидоров Петр Алексеевич', '1980-01-10', '+79759132649', 'petro21@mail.ru', 'Склад', 'Грузчик', 45000.00);

-- ==========================================
-- 		ПРОСТЫЕ ЗАПРОСЫ
-- ==========================================

-- 1. Посмотреть всех сотрудников
SELECT * FROM employees;

-- 2. Найти только тех, кто сейчас работает (активные)
SELECT full_name, position, salary 
FROM employees 
WHERE is_active = TRUE;

-- 3. Узнать возраст сотрудника (вычисляем на лету из даты рождения)
-- TIMESTAMPDIFF(YEAR, дата_рождения, текущая_дата)
SELECT 
    full_name, 
    birth_date,
    TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) AS age_years
FROM employees;

-- 4. Показать сотрудников из IT-отдела с зарплатой выше 60000
SELECT full_name, salary 
FROM employees 
WHERE department = 'IT' AND salary > 60000;

-- 5. "Уволить" сотрудника (пометить как неактивного)
-- Например, увольняем Сидорова (у него ID = 4)
UPDATE employees 
SET is_active = FALSE 
WHERE id = 4;

-- Проверка: теперь Сидоров не появится в списке активных
SELECT * FROM employees WHERE is_active = TRUE;
