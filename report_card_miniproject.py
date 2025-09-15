# Function to calculate grade based on average marks
def grade_calculator(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Function to generate and print a report card
def generate_report_card(name, roll_number, marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    grade = grade_calculator(average_marks)
    status = "PASS" if average_marks >= 40 else "FAIL"

    print("\nStudents Report Card")
    print("-" * 50)
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print("-" * 50)


# Main program loop
while True:
    name = input("Enter the student name: ")
    roll_number = input("Enter the roll number of the student: ")
    marks = []

    num_subjects = int(input("Enter the number of subjects: "))
    for i in range(1, num_subjects + 1):
        mark = int(input(f"Enter the marks for subject {i}: "))
        marks.append(mark)

    generate_report_card(name, roll_number, marks)

    choice = input("\nDo you want to enter details for another student? (yes/no): ").strip().lower()
    if choice != "yes":
        print("\nReport generation completed. Program terminated.")
        break
