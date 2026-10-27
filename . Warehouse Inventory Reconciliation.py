opening = int(input("Opening stock: "))
incoming = int(input("Incoming stock: "))
dispatch = int(input("Dispatched stock: "))
closing = int(input("Actual closing stock: "))

expected = opening + incoming - dispatch

print("Expected Closing Stock =", expected)

if expected == closing:
    print("Inventory Matched")
else:
    print("Discrepancy =", closing - expected)

if closing < 50:
    print("Replenishment Required =", 100 - closing)