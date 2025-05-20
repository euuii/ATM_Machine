import os

def balance_reset():
    with open("balance.txt", "w") as f:
        f.seek(0)
        f.write("10000")

def verify_pin():
    while True:
        try:
            with open("pin.txt", "r") as f:
                pin = int(f.readline().strip())
                log_pin = int(input("Enter PIN: "))
                if log_pin == pin:
                    print("PIN verified")
                    os_pause()
                    os_clear()
                    break
                else:
                    os_clear()
                    print("PIN verification failed")
        except ValueError:
            os_clear()
            print("Invalid input, please enter only digits")

def reg_pin():
    with open("pin.txt", "w") as f:
        pin = int(input("Enter PIN: "))
        f.write(str(pin))

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
                        print("Insufficient balance.txt")
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
        try:
            choice = int(input("(1) Check Balance \n(2) Withdraw \n(3) Deposit \n(4) Exit \nInput: "))
            match choice:
                case 1:
                    os_clear()
                    check_balance()
                case 2:
                    os_clear()
                    withdraw()
                case 3:
                    os_clear()
                    deposit()
                case 4:
                    exit()
                case _:
                    os_clear()
                    print("Invalid input. Please enter a valid number.")
        except ValueError:
            os_clear()
            print("Invalid input. Please enter a provided input.")

os_clear()
# balance_reset()
menu()
# reg_pin()
# verify_pin()
# check_balance()