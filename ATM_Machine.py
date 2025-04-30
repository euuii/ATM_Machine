import os

Balance = 0
Bank = ""
Account_Number = "99 7375 4088"
PIN_reg = 0
first_name = ""
last_name = ""

def os_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def os_pause():
    if os.name == 'nt':
        os.system('pause')
    else:
        input('Press enter to continue...')

def register():
    global BIN, Account_Number, PIN_reg, first_name, last_name
    first_name = input("Please state your First Name: ").title()
    last_name = input("Last Name: ").title()
    PIN_reg = int(input("Please set-up your PIN: "))
    print(f"Thank you for using our service {first_name} {last_name}. Here is your Card Information {BIN}{Account_Number}")
    os_pause()
    os_clear()

Bank_Reg = input("What bank were you registering (BDO, BPI, etc)? ").upper()
if Bank_Reg == "BDO":
    BIN = "4231 43"
    os_clear()
    print("Welcome to BDO! We find Ways")
    register()
elif Bank_Reg == "BPI":
    BIN = "4242 01"
    os_clear()
    print("Welcome to BPI! Let's Make It Easy.")
    register()
else:
    BIN = "4251 63"
    os_clear()
    print(f"Welcome to {Bank_Reg}")
    register()

def login():
    global PIN_reg, Bank_Reg, Bank
    Bank = input("What bank you will use for transaction? ").upper()
    print("Please insert your card.")
    os_pause()
    print("Card Recognized.")
    PIN_Login = int(input("Enter your PIN.\nPIN: "))
    if PIN_Login == PIN_reg:
        print("PIN is correct")
        os_pause()
        os_clear()
        if Bank == Bank_Reg:
            same_bank()
        else:
            different_bank()
    else:
        print("PIN is incorrect. Please try again.")
        os_pause()
        os_clear()
        login()

def same_bank():
    Input = input(f"Welcome to {Bank}!\n1. Withdraw\n2. Deposit\n3. Check User Details\n4. Help\n5. Exit\nInput: ")
    if Input == "1":
        os_clear()
        withdraw()
    elif Input == "2":
        os_clear()
        deposit()
    elif Input == "3":
        os_clear()
        details()
    else:
        print("Invalid Input. Please try again.")
        os_pause()
        os_clear()
        same_bank()

def withdraw():
    global Balance
    Withdraw = int(input("Please enter your withdrawal amount: "))
    if Withdraw > Balance:
        print("You don't have sufficient balance for this transaction. Please try again")
        os_pause()
        os_clear()
        same_bank()
    else:
        Balance = Balance - Withdraw
        os_clear()
        same_bank()

def deposit():
    global Balance
    Deposit = int(input("Please enter your deposit amount: "))
    Balance = Balance + Deposit
    os_clear()
    same_bank()

def details():
    global Balance, first_name, last_name, BIN, Account_Number
    print(f"User: {first_name} {last_name}\nBalance: {Balance}\nCard Number: {BIN}{Account_Number}\nRegistered Bank: {Bank_Reg}\nCurrent Bank: {Bank}")
    os_pause()
    os_clear()
    same_bank()

def diff_menu():
    Input = input(f"Welcome to {Bank}!\n1. Withdraw\n2. Deposit\n3. Check User Details\n4. Help\n5. Exit\nInput: ")
    if Input == "1":
        os_clear()
        diff_withdraw()
    elif Input == "2":
        os_clear()
        diff_deposit()
    elif Input == "3":
        os_clear()
        diff_details()
    else:
        print("Invalid Input. Please try again.")
        os_pause()
        os_clear()
        diff_menu()

def different_bank():
    print(f"We detected that you are using a different type of card from {Bank_Reg}.\nWe will be charging an additional fee for any transaction due to out-of-network operation.")
    Input = input("Press 1 to accept the additional fee before proceeding. Press any other key to exit.\nInput: ")
    if Input == "1":
        os_clear()
        diff_menu()
    else:
        print("Exiting...")
        os_pause()
        os_clear()
        login()

def diff_withdraw():
    global Balance
    Withdraw = int(input("Please enter your withdrawal amount with paper bills of 100, 500 or 1000: "))
    if Withdraw % 100 == 0:
        Add_Fee = 18
        Input = input(f"The selected amount for withdrawal is {Withdraw} + {Add_Fee}(Additional Fee).\nInput 1 to proceed. Otherwise, input anything\nInput: ")
        if Input == "1":
            if Withdraw + Add_Fee > Balance:
                print("You don't have sufficient balance for this transaction. Please try again")
                os_pause()
                os_clear()
                diff_menu()
            else:
                Balance = Balance - (Withdraw + Add_Fee)
                os_clear()
                diff_menu()
        else:
            print("Exiting...")
            os_pause()
            os_clear()
            diff_menu()
    else:
        print("Invalid Amount. Please try again.")
        diff_withdraw()

def diff_deposit():
    global Balance
    Deposit = int(input("Please enter your deposit amount: "))
    Add_Fee = Deposit * 0.01
    Input = input(f"The selected amount for deposit is {Deposit} - {Add_Fee}(Additional Fee).\nInput 1 to proceed. Otherwise, input anything\nInput: ")
    if Input == "1":
        Balance = Balance + (Deposit - Add_Fee)
        os_clear()
        diff_menu()
    else:
        print("Exiting...")
        os_pause()
        os_clear()
        diff_menu()

def diff_details():
    global Balance, first_name, last_name, BIN, Account_Number
    print(f"User: {first_name} {last_name}\nBalance: {Balance}\nCard Number: {BIN}{Account_Number}\nRegistered Bank: {Bank_Reg}\nCurrent Bank: {Bank}")
    os_pause()
    os_clear()
    diff_menu()

login()