import locale

def menu():
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    choice = 0

    while True:
        print("КАЛЬКУЛЯТОР")
        print("--- МЕНЮ ---")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Деление")
        print("4. Умножение")
        print("5. Выход")
        print("Ваш выбор: ", end='')

        choice = int(input())

        if choice == 1:
            print("Вы выбрали 1-ю опцию")
            return choice
        elif choice == 2:
            print("Вы выбрали 2-ю опцию")
            return choice
        elif choice == 3:
            print("Вы выбрали 3-ю опцию")
            return choice
        elif choice == 4:
            print("Вы выбрали 3-ю опцию")
            return choice
        elif choice == 5:
            print("Выход из программы...")
            break
        else:
            print("Ошибка")
            print("Выберите один пункт из меню")
