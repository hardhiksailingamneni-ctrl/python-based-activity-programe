subjects = int(input("Enter number of subjects: "))
total = 0
pass_mark = 35
grace = 5
result = "Pass"

for i in range(subjects):
    mark = int(input(f"Enter marks of subject {i+1}: "))

    if mark < pass_mark:
        if mark + grace >= pass_mark:
            mark = pass_mark
            print("Grace marks applied.")
        else:
            result = "Fail"

    total += mark

percentage = total / subjects

if percentage >= 75:
    division = "Distinction"
elif percentage >= 60:
    division = "First Class"
elif percentage >= 50:
    division = "Second Class"
else:
    division = "Pass"

print("Result:", result)
print("Percentage:", percentage)
print("Classification:", division)
