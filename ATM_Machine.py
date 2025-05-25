import os

bank = ""
current_bank = ""

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

def balance_reset(): #Instruction 1: should have an initial balance of 10,000
    with open("balance.txt", "w") as f:
        f.seek(0)
        f.write("10000")

def start():
    os_clear()
    while True:
        choice = input("New user? [y/n/...? shows all option] default (y): ").lower() #Instruction 2: should consider new or current user
        if choice == "y" or choice == "":
            balance_reset()
            os_clear()
            reg_bank()
        elif choice == "n":
            verify_pin()
        elif choice == "?":
            print("y: Yes, register new user \nn: No, login previous user")
        else:
            os_clear()
            print(f": Invalid answer '{choice}'")

def reg_bank():
    while True:
        global bank
        choice = input("Registration \n[1] Landbank \n[2] BPI \n[3] DBP \n[4] BDO \nBank: ") #Instruction 3: should consider different banks (Landbank, BPI, DBP and BDO)
        if choice == "1":
            bank = "Landbank"
            os_clear()
            reg_pin()
            return
        elif choice == "2":
            bank = "BPI"
            os_clear()
            reg_pin()
            return
        elif choice == "3":
            bank = "DBP"
            os_clear()
            reg_pin()
            return
        elif choice == "4":
            bank = "BDO"
            os_clear()
            return
        else:
            os_clear()
            print("Invalid input. Please enter a provided input.")

def reg_pin():
    print(f"Welcome to {bank} ATM")
    while True:
        pin = input("Enter PIN (6 digits): ")
        if len(pin) == 6 and pin.isdigit():
            with open(f"pin.txt", "w") as f:
                f.write(pin)
            os_clear()
            log_bank()
            return
        elif not pin.isdigit():
            os_clear()
            print("PIN must be digits")
        else:
            os_clear()
            print("PIN must be 6 digits")

def log_bank():
    while True:
        global current_bank
        choice = input("Bank to use for transaction \n[1] Landbank \n[2] BPI \n[3] DBP \n[4] BDO \nBank: ") #Instruction 3: should consider different banks (Landbank, BPI, DBP and BDO)
        if choice == "1":
            current_bank = "Landbank"
            os_clear()
            verify_pin()
            return
        elif choice == "2":
            current_bank = "BPI"
            os_clear()
            verify_pin()
            return
        elif choice == "3":
            current_bank = "DBP"
            os_clear()
            verify_pin()
            return
        elif choice == "4":
            current_bank = "BDO"
            os_clear()
            verify_pin()
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
            amount = input("Withdraw amount: ")
            if amount.isdigit():
                amount = int(amount)
                if amount % 100 == 0 and amount > 0:
                    if amount <= balance:
                        f.seek(0)
                        if bank == current_bank:
                            balance = balance - amount
                        else: #Instruction 4: if the user has a different bank, will charge P18.00 for each "withdraw"
                            choice = input(f"You will be deducted an additional P18 for out-of-network transaction. \nRegistered Bank: {bank}\nCurrent Bank: {current_bank}\nProceed? [y/n]: ").lower()
                            while True:
                                if choice == "y" or choice == "":
                                    if (amount + 18) <= balance:
                                        balance = balance - (amount + 18)
                                        break
                                    else:
                                        os_clear()
                                        print("Insufficient Fund")
                                        return
                                else:
                                    os_clear()
                                    print("Enter a valid choice.")
                        f.write(str(balance))
                        f.truncate()
                        check_balance()
                        return
                    else:
                        os_clear()
                        print("Insufficient Fund")
                        os_pause()
                        os_clear()
                else:
                    os_clear()
                    print("Invalid Amount")
            else:
                os_clear()
                print("Invalid input. Please enter a valid number.")

def deposit():
    with open("balance.txt", "r+") as f:
        balance = int(f.read().strip())
        while True:
            amount = input("Enter the amount you want to deposit: ")
            if amount.isdigit():
                amount = int(amount)
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
            else:
                os_clear()
                print("Invalid input. Please enter a valid number.")

# os_clear()
# balance_reset()
# menu()
# reg_pin()
# verify_pin()
# check_balance()
# reg_bank()
start()