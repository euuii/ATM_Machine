Balance = 1000

Deposit = int(input("Please enter your deposit amount: "))
Add_Fee = Deposit * 0.01
Input = input(f"The selected amount for deposit is {Deposit} - {Add_Fee}(Additional Fee).\nInput 1 to proceed. Otherwise, input anything\nInput: ")
if Input == "1":
    Balance = Balance + (Deposit - Add_Fee)
else:
    print("YOU GAY")

print(Balance)