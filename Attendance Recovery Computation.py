attended = int(input("Classes attended: "))
total = int(input("Total classes: "))
target = 75

attendance = (attended / total) * 100
print("Current Attendance =", attendance)

future = 0

while (attended / total) * 100 < target:
    attended += 1
    total += 1
    future += 1

print("Minimum extra classes needed:", future)