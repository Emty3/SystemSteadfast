name_user = input("Введите ваше имя: ")
age_user = int(input("Введите ваш возраст: "))

if age_user >= 18:
    print(f"Добро пожаловать, {name_user}!")
else:
    print(f"Извините, {name_user}, доступ разрешён только с 18 лет.")
