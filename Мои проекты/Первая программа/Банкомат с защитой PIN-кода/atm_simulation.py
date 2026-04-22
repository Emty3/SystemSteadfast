# atm_simulation.py

# --- НАСТРОЙКИ ---
CORRECT_PIN = "1234"
INITIAL_BALANCE = 5000.0
MAX_ATTEMPTS = 3

print("--- 🏦 Банкомат v1.0 ---")

# --- ЭТАП 1: АВТОРИЗАЦИЯ ---
attempts = 0
is_authenticated = False # Флаг: вошел ли пользователь?

while attempts < MAX_ATTEMPTS:
    pin = input(f"Введите PIN-код (осталось попыток: {MAX_ATTEMPTS - attempts}): ")
    
    if pin == CORRECT_PIN:
        print("✅ PIN-код верен! Добро пожаловать.")
        is_authenticated = True
        break # Прерываем цикл проверки PIN-кода
    else:
        attempts += 1
        print("❌ Неверный PIN-код.")

# Если после цикла флаг все еще False, значит попытки кончились
if not is_authenticated:
    print("🚫 Карта заблокирована. Обратитесь в банк.")
else:
    # --- ЭТАП 2: МЕНЮ ОПЕРАЦИЙ ---
    balance = INITIAL_BALANCE
    
    while True: # Бесконечный цикл, выходим через 'break'
        print("\n--- Меню ---")
        print(f"💰 Баланс: {balance:.2f} руб.")
        print("1. Снять наличные")
        print("2. Пополнить счет")
        print("3. Выйти")
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == "1":
            try:
                amount = float(input("Сумма снятия: "))
                if amount > balance:
                    print("❌ Недостаточно средств!")
                elif amount <= 0:
                    print("❌ Сумма должна быть положительной!")
                else:
                    balance -= amount
                    print(f"✅ Выдали {amount:.2f} руб. Остаток: {balance:.2f}")
            except ValueError:
                print("❌ Введите число!")
                
        elif choice == "2":
            try:
                amount = float(input("Сумма пополнения: "))
                if amount > 0:
                    balance += amount
                    print(f"✅ Зачислено {amount:.2f} руб. Баланс: {balance:.2f}")
                else:
                    print("❌ Сумма должна быть положительной!")
            except ValueError:
                print("❌ Введите число!")
                
        elif choice == "3":
            print("👋 Спасибо за использование банкомата!")
            break # Выход из бесконечного цикла
            
        else:
            print("⚠️ Неверный выбор. Попробуйте снова.")