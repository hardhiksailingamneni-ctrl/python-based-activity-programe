subjects = int(input("Number of subjects: "))

for i in range(subjects):
    exam1 = int(input("Exam1 marks: "))
    exam2 = int(input("Exam2 marks: "))

    change = exam2 - exam1

    if change > 0:
        print("Improved by", change)
    elif change < 0:
        print("Declined by", abs(change))
    else:
        print("No Change")