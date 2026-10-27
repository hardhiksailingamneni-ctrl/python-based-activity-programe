vehicles = int(input("Number of vehicles: "))
distance = float(input("Distance (km): "))
fuel_price = float(input("Fuel price per litre: "))

lowest_cost = 999999
best_vehicle = 0

for i in range(vehicles):
    mileage = float(input(f"Vehicle {i+1} mileage: "))

    fuel = distance / mileage
    cost = fuel * fuel_price

    print("Fuel Needed =", fuel)
    print("Cost =", cost)

    if cost < lowest_cost:
        lowest_cost = cost
        best_vehicle = i + 1

print("Best Vehicle =", best_vehicle)