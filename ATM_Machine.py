def withdraw():
    with open("balance", "r+") as f:
        content = f.read().strip()
        balance = float(content)
        while True:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= balance:
                f.seek(0)
                balance = balance - amount
                f.write(str(balance))
                print(balance)
                break
withdraw()