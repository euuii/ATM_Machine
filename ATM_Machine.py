Balance = 0
Bank = ""
Account_Number = "99 7375 4088"
PIN_reg = 0

def register():
    global BIN, Account_Number, PIN_reg
    first_name = input("Please state your First Name: ").title()
    last_name = input("Last Name: ").title()
    PIN_reg = int(input("Please set-up your PIN: "))
    print(f"Thank you for using our service {first_name} {last_name}. Here is your Card Information {BIN}{Account_Number}")

Bank_Reg = input("What bank were you registering (BDO, BPI, etc)? ").upper()
if Bank_Reg == "BDO":
    BIN = "4231 43"
    print("Welcome to BDO! We find Ways")
    register()
elif Bank_Reg == "BPI":
    BIN = "4242 01"
    print("Welcome to BPI! Let's Make It Easy.")
    register()
else:
    BIN = "4251 63"
    print(f"Welcome to {Bank_Reg}")
    register()

def login():
    global Bank, PIN_reg
    Bank = input("What bank you will use for transaction? ").upper()
    PIN_Login = int(input("Insert your card and enter your PIN.\nPIN: "))
    if PIN_Login == PIN_reg:
        print("PIN is correct")
        if Bank == Bank_Reg:
            same_bank()
        else:
            different_bank()
    else:
        print("PIN is incorrect")
        login()

def same_bank():
    Input = input(f"Welcome to {Bank}!\n1. Withdraw\n2. Deposit\n3. Check User Details\n4. Help\n5. Exit\nInput: ")
    if Input == "1":
        withdraw()
    elif Input == "2":
        deposit()
    else:
        print("Invalid Input. Please try again.")
        same_bank()

def withdraw():
    global Balance
    Withdraw = int(input("Please enter your withdrawal amount: "))
    if Withdraw > Balance:
        print("You don't have sufficient balance for this transaction.")
    else:
        Balance = Balance - Withdraw

def deposit():
    global Balance
    Deposit = int(input("Please enter your deposit amount: "))
    Balance = Balance + Deposit
    same_bank()

def diff_menu():
    Input = input(f"Welcome to {Bank}!\n1. Withdraw\n2. Deposit\n3. Check User Details\n4. Help\n5. Exit\nInput: ")
    if Input == "1":
        diff_withdraw()
    elif Input == "2":
        diff_deposit()
    else:
        print("Invalid Input. Please try again.")
        diff_menu()

def different_bank():
    print(f"We detected that you are using a different type of card from {Bank_Reg}.\nWe will be charging an additional fee for any transaction due to out-of-network operation.")
    Input = input("Press 1 to accept the additional fee before proceeding. Press any other key to exit.\nInput: ")
    if Input == "1":
        diff_menu()
    else:
        login()

def diff_withdraw():
    global Balance
    Withdraw = int(input("Please enter your withdrawal amount: "))
    Add_Fee = Withdraw * 0.01
    Input = input(f"The selected amount for withdrawal is {Withdraw} + {Add_Fee}(Additional Fee).\nInput 1 to proceed. Otherwise, input anything\nInput: ")
    if Input == "1":
        if Withdraw + Add_Fee > Balance:
            print("You don't have sufficient balance for this transaction.")
            diff_menu()
        else:
            Balance = Balance - (Withdraw + Add_Fee)
            diff_menu()
    else:
        diff_menu()

def diff_deposit():
    global Balance
    Deposit = int(input("Please enter your deposit amount: "))
    Add_Fee = Deposit * 0.01
    Input = input(f"The selected amount for deposit is {Deposit} - {Add_Fee}(Additional Fee).\nInput 1 to proceed. Otherwise, input anything\nInput: ")
    if Input == "1":
        Balance = Balance + (Deposit - Add_Fee)
        diff_menu()
    else:
        diff_menu()

login()