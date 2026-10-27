entry = int(input("Entry hour (0-23): "))
exit = int(input("Exit hour (0-23): "))

if exit < entry:
    hours = (24 - entry) + exit
else:
    hours = exit - entry

vehicle = input("Vehicle (Car/Bike): ")

if vehicle == "Car":
    rate = 30
else:
    rate = 15

fee = hours * rate

print("Parking Hours =", hours)
print("Parking Fee =", fee)