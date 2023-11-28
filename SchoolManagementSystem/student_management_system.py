students = []
HELP_MSG = {
    'add': "add to create the student",
    'view all': "View all the student",
    'update': "update student by roll number",
    'delete': "delete student with the roll number",
    'sort': "sort the student list by marks",
}


class Student:
    roll_no = 0

    def __init__(self, name, marks):
        Student.roll_no += 1
        self.name = name
        self.roll_no = Student.roll_no
        self.marks = marks

    def __repr__(self):
        return self.name


def add_students():
    while True:
        try:
            student_name = input("Enter a student name or 'exit' to stop adding the student: ")
            if student_name.lower() == "exit":
                break
            student_mark = float(input("Enter the student marks: "))
            new_student = Student(student_name, student_mark)
            students.append(new_student)
        except ValueError:
            print("The student name should be string and marks should be in float or int")


def view_student_detail():
    if not students:
        print("Student list is empty")
    else:
        for student in students:
            print(f"Name: {student.name} \n Roll No: {student.roll_no} \n Marks: {student.marks}")
            print()


def search_student(roll_no):
    if not students:
        print("Student list is empty")
    else:

        found = False
        for student in students:
            if student.roll_no == roll_no:
                print(f"Name: {student.name} \n Roll No: {student.roll_no} \n Marks: {student.marks}")
                found = True
                break
        if not found:
            print(f'Student with the {roll_no} not found')


def sort_student():
    students.sort(key=lambda student: student.marks, reverse=True)


def update_student_detail(roll_no):
    if not students:
        print("Student list is empty")
    else:
        found = False
        for student in students:
            if student.roll_no == roll_no:
                try:
                    new_name = input("enter a new name or leave it to keep old name: ")
                    marks = float(input("Update a student mark or leave it to keep old mark: "))
                    if new_name or marks:
                        if new_name:
                            student.name = new_name
                        if marks:
                            student.marks = marks
                        found = True
                        print("Student details updated successfully")
                        break
                    else:
                        print("No changes made")

                except ValueError:
                    print("The student name should be string and marks should be either float or int")

        if not found:
            print(f'Student with the {roll_no} not found')


def delete_student(roll_number):
    if not students:
        print("Student list is empty")

    else:
        found = False

        for student in students:
            if student.roll_no == roll_number:
                students.remove(student)
                found = True
                break
        if not found:
            print("Roll number not found")


def help_message():
    for operation, msg in HELP_MSG.items():
        print(operation, msg, sep="-->")


exit_program = False
help_message()
while not exit_program:
    user_operation = input("what do you want to do: ").lower()
    if user_operation == "add":
        add_students()
    elif user_operation == "delete":
        try:
            roll_number = int(input("Student roll number"))
            delete_student(roll_number)
        except ValueError:
            print("Roll number should be integer")

    elif user_operation == "sort":
        sort_student()
    elif user_operation == "update":
        try:
            roll_number = int(input("Student roll number"))
            update_student_detail(roll_number)
        except ValueError:
            print("Roll number should be integer")

    elif user_operation == "view all":
        view_student_detail()

    elif user_operation == "exit":
        exit_program = True
    else:

        print("Invalid operation")
