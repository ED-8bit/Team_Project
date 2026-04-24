import minus
import plus
import delen
import mult
import operations_menu

def main():
    while True:
        choice = menu()
        
        if choice == '0':
            print("Закрытие")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                
                if choice == '1':
                    result = plus(a, b)
                elif choice == '2':
                    result = minus(a, b)
                elif choice == '3':
                    result = mult(a, b)
                elif choice == '4':
                    result = delen(a, b)

                print(f"Результат: {result}\n")
            except ValueError:
                print("Ошибка: введите числа!\n")
        else:
            print("Неверный выбор. Попробуйте снова.\n")