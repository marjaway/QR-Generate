import segno
from colorama import init
from colorama import Fore 
init()

def main():
    input("Press Enter to return...")

def returnn():
    input(Fore.RESET + "\nContinue (Press Enter)\n")

def error():
    input(Fore.RED + "error... Press Enter to go back\n" + Fore.RESET)
    

def save():
    print(Fore.GREEN + "The QR code has been generated. Saved to the folder where the program is located" + Fore.RESET)


while True:
    print('''QR code generator\n                                           
⠀[ 1 ] - Start generating
⠀[ 2 ] - Author⠀⠀
⠀[ 3 ] - Log out
''')
    
    command = input(Fore.CYAN + f"\nSelect a command:{Fore.RESET} ")
    
    if command == "1":
        print(Fore.RESET + '''
    [ 1 ] - Regular QR code (colors will be: white and black)
    [ 2 ] - Multicolored QR code\n''')
        
        commandqr = input(Fore.CYAN + f"Select a command:{Fore.RESET} ")
        
        if commandqr == "1":
            qrcod = input(Fore.RESET + "\nEnter the link for the QR code: ")
            qrcode = segno.make_qr(f"{qrcod}")

            print('''\nWhat format should I save it in?
                1. PNG
                2. SVG
                3. PDF''')
            try:
                
                photo = input("\n[ ? ] - Select format: ")
                nameqr = input("\nEnter a name for the QR code:: ")

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
                    print(Fore.RED + "It is necessary to select the format in which the QR code will be saved\n")
            except ValueError:
                error()
        elif commandqr == "2":
            print(Fore.RESET + '''
    [ 1 ] - Black
    [ 2 ] - Grey
    [ 3 ] - Blue
    [ 4 ] - Red
    [ 5 ] - Your own option
    [ 6 ] - Return''')
            
            colorqr = input(Fore.CYAN + f"\nSelect a command:{Fore.RESET} ")
            try:
                if colorqr == "1":
                    nameqr = input("Enter a name for the QR code: ")
                    qrcod = input(Fore.RESET + "\nEnter the link for the QR code: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark=None, light='black', scale=10)
                    save()
                elif colorqr == "2":
                    nameqr = input("Enter a name for the QR code: ")
                    qrcod = input(Fore.RESET + "\nEnter the link for the QR code: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', light=None, scale=10)
                    save()
                elif colorqr == "3":
                    nameqr = input("Enter a name for the QR code: ")
                    qrcod = input(Fore.RESET + "\nEnter the link for the QR code: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark='#00fc', scale=10)
                    save()
                elif colorqr == "4":
                    nameqr = input("Enter a name for the QR code: ")
                    qrcod = input(Fore.RESET + "\nEnter the link for the QR code: ")
                    qrcode = segno.make_qr(f"{qrcod}")
                    qrcode.save(f'{nameqr}.png', dark='#ff0000', scale=10)
                    save()
                elif colorqr == "5":
                    nameqr = input("Enter a name for the QR code: ")
                    qrcod = input(Fore.RESET + "\nEnter the link for the QR code: ")
                    color = input("\nEnter color code in format #000000: ")
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
        print(Fore.RESET + 'Author of the program: marjaway\n')
        main()
    elif command == "3":
        break
    else:
        error()