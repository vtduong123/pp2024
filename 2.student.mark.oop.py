class Student:
    def __init__(self, student_id, student_name, dob):
        self.__id = student_id
        self.__name = student_name
        self.__DOB = dob
        self.__marks = {}

    def input_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def set_id(self, student_id):
        self.__id = student_id

    def set_name(self, student_name):
        self.__name = student_name

    def set_dob(self, dob):
        self.__DOB = dob


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name


class Listing:
    def __init__(self):
        self.students = []
        self.courses = []

    def list_students(self):
        if not self.students:
            print("There aren't any students!")
        else:
            print("Student List:")
            for i, student in enumerate(self.students):
                print(f"{i + 1}. ID: {student._Student__id} - Name: {student._Student__name} - DoB: {student._Student__DOB}")
                if student._Student__marks:
                    print("   Marks (Course Id - Mark): ", student._Student__marks)

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses!")
        else:
            print("Course List:")
            for i, course in enumerate(self.courses):
                print(f"{i + 1}. ID: {course.id} - Name: {course.name}")

def main():
    school_listing = Listing()

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
            student = Student(input("Enter Student ID: "), input("Enter Student Name: "), input("Enter Student Date of Birth (DoB): "))
            school_listing.students.append(student)
        elif option == 2:
            course = Course(input("Enter Course ID: "), input("Enter Course Name: "))
            school_listing.courses.append(course)
        elif option == 3:
            student_index = int(input("Enter student index to enter mark: ")) - 1
            course_id = input("Enter Course ID to enter mark for the student: ")
            mark = float(input("Enter Mark for the student: "))
            school_listing.students[student_index].input_mark(course_id, mark)
        elif option == 4:
            school_listing.list_students()
        elif option == 5:
            school_listing.list_courses()
        else:
            print("Invalid input. Please try again!")


if __name__ == "__main__":
    main()
