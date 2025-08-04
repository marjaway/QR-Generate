import segno
from colorama import init
from colorama import Fore 
init()

def main():
    input("Нажмите Entert, чтобы вернуться...")

def returnn():
    input(Fore.RESET + "\nПродолжить (Нажмите Enter)\n")

def error():
    input(Fore.RED + "Ошибка... Нажмите Enter, чтобы вернуться\n" + Fore.RESET)
    

def save():
    print(Fore.GREEN + "QR-код был сгенерирован. Сохраненно в папку где находиться программа" + Fore.RESET)


while True:
    print('''Генератор QR-кодов\n                                           
⠀[ 1 ] - Начать генерацию⠀
⠀[ 2 ] - Автор⠀⠀
⠀[ 3 ] - Выйти
''')
    
    command = input(Fore.CYAN + f"\nВыберете команду:{Fore.RESET} ")
    
    if command == "1":
        print(Fore.RESET + '''
    [ 1 ] - Обычный QR-код ( цвета будут: белый и черный )
    [ 2 ] - Разноцветный QR-код\n''')
        
        commandqr = input(Fore.CYAN + f"Выберете команду:{Fore.RESET} ")
        
        if commandqr == "1":
            qrcod = input(Fore.RESET + "\nВведите ссылку для QR-кода: ")
            qrcode = segno.make_qr(f"{qrcod}")

            print('''\nВ каком формате сохранить?
                1. PNG
                2. SVG
                3. PDF''')
            try:
                
                photo = input("\n[ ? ] - Выберете формат: ")
                nameqr = input("\nВведите название для qr-кода: ")

                if photo == "1":
                    qrcode.save(f"{nameqr}.png", scale=10)
                    save()
                elif photo == "2":
                    qrcode.save(f"{nameqr}.svg", scale=10)
                    save()
                elif photo == "3":
                    qrcode.save(f"{nameqr}.pdf", scale=10)
                    save()
                else:
                    print(Fore.RED + "Нужно обязательно выбрать формат, в котором сохранится QR-code\n")
            except ValueError:
                error()
        elif commandqr == "2":
            print(Fore.RESET + '''
    [ 1 ] - Черный
    [ 2 ] - Серый
    [ 3 ] - Синий
    [ 4 ] - Красный
    [ 5 ] - Свой вариант
    [ 6 ] - Выйти''')
            
            colorqr = input(Fore.CYAN + f"\nВыберете команду:{Fore.RESET} ")
            try:
                if colorqr == "1":
                    nameqr = input("Введите название для qr-кода: ")
                    qrcod = input(Fore.RESET + "\nВведите ссылку для QR-кода: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark=None, light='black', scale=10)
                    save()
                elif colorqr == "2":
                    nameqr = input("Введите название для qr-кода: ")
                    qrcod = input(Fore.RESET + "\nВведите ссылку для QR-кода: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', light=None, scale=10)
                    save()
                elif colorqr == "3":
                    nameqr = input("Введите название для qr-кода: ")
                    qrcod = input(Fore.RESET + "\nВведите ссылку для QR-кода: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark='#00fc', scale=10)
                    save()
                elif colorqr == "4":
                    nameqr = input("Введите название для qr-кода: ")
                    qrcod = input(Fore.RESET + "\nВведите ссылку для QR-кода: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark='#ff0000', scale=10)
                    save()
                elif colorqr == "5":
                    nameqr = input("Введите название для qr-кода: ")
                    qrcod = input(Fore.RESET + "\nВведите ссылку для QR-кода: ")
                    color = input("\nВведите цветой код в формате #000000: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark=f'{color}', scale=10)
                    save()
                elif colorqr == "6":
                    main()
                else:
                    error()   
            except ValueError:
                error()          
        else:
            error()
        returnn()
    
    elif command == "2":
        print(Fore.RESET + 'Автор программы: marjaway\n')
        main()
    elif command == "3":
        break
    else:
        error()