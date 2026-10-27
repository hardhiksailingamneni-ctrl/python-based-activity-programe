capacity = 1000
water = int(input("Initial water amount: "))

days = int(input("Number of days: "))

for d in range(days):
    inflow = int(input("Inflow: "))
    outflow = int(input("Outflow: "))

    water = water + inflow - outflow

    if water > capacity:
        print("Overflow on day", d + 1)
        water = capacity

    if water < 0:
        print("Tank Empty on day", d + 1)
        water = 0

    print("Water Level =", water)