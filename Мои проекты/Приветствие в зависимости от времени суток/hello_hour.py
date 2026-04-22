age_user = int(input("Введите ваш возрост"))
if age_user >= 18:
    print("Добро пожаловать!!!")
else:
    print("Уйди прочь")hour = int(input("Который час? (0-23): "))
if hour >= 6 and hour < 12:
    print("☀️ Доброе утро!")
elif hour >= 12 and hour < 18:
    print("🌞 Добрый день!")
elif hour >= 18 and hour < 23:
    print("🌙 Добрый вечер!")
else:
    print("🌃 Доброй ночи!")
