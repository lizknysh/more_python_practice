subjects = ["Python", "Cloud Computing", "Networking", "Database", "DevOps"]
num_students = int(input("How many students? "))

# Class summary counters 
a_students = 0
b_students = 0
c_students = 0
d_students = 0
failed_students = 0

for student in range(num_students):
    print("\n--- Student", student + 1, "---")
    name = input("Enter student's name: ")

    marks = []
    failed_subjects = 0

    # Ask for input for each subject
    for subject in subjects:
        while True:
            mark = float(input("Enter mark for " + subject + ": "))

            if mark >= 0 and mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid mark")

    # Calculate results
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Determine grade
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display individual subject performance
    print("\n-----", name + "'s Report -----")

    for i in range(len(subjects)):

        if marks[i] >= 90:
            print("Excellent performance in", subjects[i])

        elif marks[i] >= 75:
            print("Very good performance in", subjects[i])

        elif marks[i] >= 60:
            print("Good performance in", subjects[i])

        elif marks[i] >= 50:
            print("Passed", subjects[i])

        else:
            print("Failed", subjects[i])
            failed_subjects += 1
        print(subjects[i], ":", marks[i])

    # Display student's results
    print("\n--- Results for", name, "---")
    print("Total marks:", total)
    print("Average percentage:", round(average, 2), "%")
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)
    print("Failed subjects:", failed_subjects)
    print("Final grade:", grade)

    # Overall result
    if failed_subjects >= 2:
        print("Result: FAILED - Too many failed subjects")
        failed_students += 1
    else:
        print("Result: PASSED")

        # Count students by grade
        if grade == "A+" or grade == "A":
            a_students += 1

        elif grade == "B":
            b_students += 1

        elif grade == "C":
            c_students += 1

        elif grade == "D":
            d_students += 1

# Class summary
print("\n== CLASS SUMMARY ==")
print("Total Students:", num_students)
print("A+/A Students:", a_students)
print("B Students:", b_students)
print("C Students:", c_students)
print("D Students:", d_students)
print("Failed Students:", failed_students)