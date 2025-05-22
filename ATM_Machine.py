import os

bank = ""

def balance_reset():
    with open("balance.txt", "w") as f:
        f.seek(0)
        f.write("10000")

def start():
    os_clear()
    while True:
        choice = input("Create new user? [y/n]: ").lower()
        match choice:
            case "y":
                balance_reset()
                os_clear()
                reg_bank()
            case "n":
                verify_pin()
            case _:
                os_clear()
                print(f": Invalid answer '{choice}'")

def reg_bank():
    while True:
        global bank
        choice = input("Choose bank \n[1] Landbank \n[2] BPI \n[3] DBP \n[4] BDO \nInput: ")
        if choice == "1":
            bank = "Landbank"
            os_clear()
            print(f"Welcome to {bank} ATM")
            return
        elif choice == "2":
            bank = "BPI"
            os_clear()
            print(f"Welcome to {bank} ATM")
            return
        elif choice == "3":
            bank = "DBP"
            os_clear()
            print(f"Welcome to {bank} ATM")
            return
        elif choice == "4":
            bank = "BDO"
            os_clear()
            print(f"Welcome to {bank} ATM")
            return
        else:
            os_clear()
            print("Invalid input. Please enter a provided input.")

def verify_pin():
    while True:
        with open("pin.txt", "r") as f:
            pin = f.readline().strip()
            log_pin = input("Enter login pin number: ")
            if len(log_pin) == 6 and log_pin.isdigit():
                if log_pin == pin:
                    os_clear()
                    menu()
                    return
                else:
                    os_clear()
                    print("Wrong PIN")
            elif not log_pin.isdigit():
                os_clear()
                print("PIN must be digits")
            else:
                os_clear()
                print("PIN must be 6 digits")

def reg_pin():
    while True:
            pin = input("Enter PIN (6 digits): ")
            if len(pin) == 6 and pin.isdigit():
                with open(f"pin.txt", "w") as f:
                    f.write(pin)
                os_clear()
                verify_pin()
                return
            elif not pin.isdigit():
                os_clear()
                print("PIN must be digits")
            else:
                os_clear()
                print("PIN must be 6 digits")

def os_clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def os_pause():
    if os.name == "nt":
        os.system("pause")
    else:
        input("Press enter to continue...")

def check_balance():
    with open("balance.txt", "r") as f:
        balance = f.readline().strip()
        print(f"Your balance is: {balance}")
        os_pause()
        os_clear()
        return

def withdraw():
    with open("balance.txt", "r+") as f:
        balance = int(f.read().strip())
        while True:
            try:
                amount = int(input("Withdraw amount: "))
                if amount % 100 == 0 and amount > 0:
                    if amount <= balance:
                        f.seek(0)
                        balance = balance - amount
                        f.write(str(balance))
                        f.truncate()
                        check_balance()
                        return
                    else:
                        os_clear()
                        print("Insufficient balance")
                else:
                    os_clear()
                    print("Invalid Amount")
            except ValueError:
                os_clear()
                print("Invalid input. Please enter a valid number.")

def deposit():
    with open("balance.txt", "r+") as f:
        balance = int(f.read().strip())
        while True:
            try:
                amount = int(input("Enter the amount you want to deposit: "))
                if amount % 100 == 0 and amount > 0:
                    f.seek(0)
                    balance = balance + amount
                    f.write(str(balance))
                    f.truncate()
                    check_balance()
                    return
                else:
                    os_clear()
                    print("The only dispensable amount is 1000, 500 and 100")
            except ValueError:
                os_clear()
                print("Invalid input. Please enter a valid number.")

def menu():
    while True:
        choice = input("[1] Check Balance \n[2] Withdraw \n[3] Deposit \n[4] Exit \nInput: ")
        if choice == "1":
            os_clear()
            check_balance()
        elif choice == "2":
            os_clear()
            withdraw()
        elif choice == "3":
            os_clear()
            deposit()
        elif choice == "4":
            os_clear()
            return
        else:
            os_clear()
            print("Invalid input. Please enter a provided input.")

# os_clear()
# balance_reset()
# menu()
# reg_pin()
# verify_pin()
# check_balance()
reg_bank()
# start()