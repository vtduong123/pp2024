# Function to input a number of units (courses / students)
def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "))

# Function to input student information
def input_student_info():
    student = {}
    student['id'] = input("Enter Student ID: ")
    student['name'] = input("Enter Student Name: ")
    student['DoB'] = input("Enter Student Date of Birth (DoB): ")
    return student

# Function to input course information
def input_course_info():
    course = {}
    course['id'] = input("Enter Course ID: ")
    course['name'] = input("Enter Course Name: ")
    return course

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
                
                
# Function to list courses
def list_courses(courses):
    if not courses:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course['id']} - {course['name']}")


# Main function
def main():
    # Initialize lists
    courses = []
    students = []

    while True:
        print("""
        0. Exit
        1. Add Student
        2. Add Course
        3. Input Mark for Student
        4. List Students
        5. List Courses
        """)
        option = int(input("Your choice: "))
        
        if option == 0:
            break
        elif option == 1:
            students.append(input_student_info())
        elif option == 2:
            courses.append(input_course_info())
        elif option == 3:
            student_index = int(input("Enter student index to enter mark: ")) - 1
            input_mark(students[student_index], courses)
        elif option == 4:
            list_students(students)
        elif option == 5:
            list_courses(courses)
        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()