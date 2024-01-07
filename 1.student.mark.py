# Function to input a number of units (courses / students)
def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "))

# Function to input information for a type (student/course info)
def input_infos(args):
    item = {}
    item['id'] = input("Enter ID: ")
    item['name'] = input("Enter Name: ")
    item['DoB'] = input("Enter Date of Birth (DoB): ")
    return item

# Function to input student marks based on the course id
def input_mark(student, courses):
    course_id = int(input("Enter Course ID to enter mark for the student: "))
    mark = float(input("Enter Mark for the student: "))
    student["marks"][course_id] = mark

# Function to list students
def list_students(students):
    if not students:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for i, student in enumerate(students):
            print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")
            if "marks" in student:
                print("Marks (Course Id - Mark): ", student["marks"])