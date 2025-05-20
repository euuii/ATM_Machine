import os

def balance_reset():
    with open("balance", "w") as f:
        f.seek(0)
        f.write("10000")

def os_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def os_pause():
    if os.name == 'nt':
        os.system('pause')
    else:
        input('Press enter to continue...')

def withdraw():
    with open("balance", "r+") as f:
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
                        print(f"Your balance is now {balance}")
                        os_pause()
                        os_clear()
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
    with open("balance", "r+") as f:
        balance = int(f.read().strip())
        while True:
            try:
                amount = int(input("Enter the amount you want to deposit: "))
                if amount % 100 == 0 and amount > 0:
                    f.seek(0)
                    balance = balance + amount
                    f.write(str(balance))
                    f.truncate()
                    print(f"Your balance is now {balance}")
                    os_pause()
                    os_clear()
                    return
                else:
                    os_clear()
                    print("We only accept 100, 500 and 1000 cash")
            except ValueError:
                os_clear()
                print("Invalid input. Please enter a valid number.")

def menu():
    while True:
        try:
            choice = int(input("(1) Withdraw \n(2) Deposit \n(3) Exit \nInput: "))
            match choice:
                case 1:
                    os_clear()
                    withdraw()
                case 2:
                    os_clear()
                    deposit()
                case 3:
                    exit()
                case _:
                    os_clear()
                    print("Invalid input. Please enter a valid number.")
        except ValueError:
            os_clear()
            print("Invalid input. Please enter a provided input.")

os_clear()
balance_reset()
menu()