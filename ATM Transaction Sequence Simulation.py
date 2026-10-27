balance = 1000

n = int(input("Number of transactions: "))

for i in range(n):
    t = input("Deposit or Withdraw (D/W): ")

    if t == "D":
        amount = float(input("Amount: "))
        balance += amount

    elif t == "W":
        amount = float(input("Amount: "))
        if amount <= balance and amount <= 20000:
            balance -= amount
        else:
            print("Invalid withdrawal")

print("Final Balance =", balance)