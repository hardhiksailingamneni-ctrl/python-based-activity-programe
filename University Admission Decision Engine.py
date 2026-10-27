students = int(input("Number of applicants: "))

data = []

for i in range(students):
    name = input("Student Name: ")
    marks = float(input("Aggregate Marks: "))

    if marks >= 85:
        status = "Eligible"
    else:
        status = "Not Eligible"

    data.append([name, marks, status])

data.sort(key=lambda x: x[1], reverse=True)

print("\nRank List")

rank = 1
for s in data:
    print(rank, s[0], s[1], s[2])
    rank += 1