def withdraw():
    with open("balance", "r+") as f:
        content = f.read().strip()
        balance = float(content)
        while True:
            try:
                amount = int(input("Enter the amount you want to withdraw: "))
                if amount % 100 == 0:
                    if amount <= balance:
                        f.seek(0)
                        balance = balance - amount
                        f.write(str(balance))
                        f.truncate()
                        print(balance)
                        break
                else:
                    print("We only accept 100, 500 and 1000 cash")
            except ValueError:
                print("Invalid input. Please enter a number.")

withdraw()