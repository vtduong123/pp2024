import math
import curses

class Student:
    def __init__(self, student_id, student_name, dob):
        self.__id = student_id
        self.__name = student_name
        self.__DOB = dob
        self.__marks = {}

    def input_mark(self, course_id, mark):
        # Round down the mark to 1-digit decimal using math.floor
        self.__marks[course_id] = math.floor(mark)

    def set_id(self, student_id):
        self.__id = student_id

    def set_name(self, student_name):
        self.__name = student_name

    def set_dob(self, dob):
        self.__DOB = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__DOB

    def get_marks(self):
        return self.__marks


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
                print(f"{i + 1}. ID: {student.get_id()} - Name: {student.get_name()} - DoB: {student.get_dob()}")
                if student.get_marks():
                    print("   Marks (Course Id - Mark): ", student.get_marks())

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses!")
        else:
            print("Course List:")
            for i, course in enumerate(self.courses):
                print(f"{i + 1}. ID: {course.id} - Name: {course.name}")

    def calculate_gpa(self, student_index):
        student = self.students[student_index]
        marks = list(student.get_marks().values())
        if not marks:
            return 0
        total_marks = sum(marks)
        total_courses = len(marks)
        return total_marks / total_courses

    def sort_students_by_gpa_descending(self):
        self.students.sort(key=lambda student: self.calculate_gpa(self.students.index(student)), reverse=True)


def main(stdscr):
    school_listing = Listing()

    while True:
        stdscr.clear()
        stdscr.addstr("1. Add Student\n")
        stdscr.addstr("2. Add Course\n")
        stdscr.addstr("3. Input Mark for Student\n")
        stdscr.addstr("4. List Students\n")
        stdscr.addstr("5. List Courses\n")
        stdscr.addstr("0. Exit\n")
        stdscr.refresh()

        option = stdscr.getch() - ord('0')

        if option == 0:
            break
        elif option == 1:
            stdscr.addstr("Enter Student ID: ")
            student_id = stdscr.getstr().decode()
            stdscr.addstr("Enter Student Name: ")
            student_name = stdscr.getstr().decode()
            stdscr.addstr("Enter Student Date of Birth (DoB): ")
            dob = stdscr.getstr().decode()
            student = Student(student_id, student_name, dob)
            school_listing.students.append(student)
        elif option == 2:
            stdscr.addstr("Enter Course ID: ")
            course_id = stdscr.getstr().decode()
            stdscr.addstr("Enter Course Name: ")
            course_name = stdscr.getstr().decode()
            course = Course(course_id, course_name)
            school_listing.courses.append(course)
        elif option == 3:
            stdscr.addstr("Enter student index to enter mark: ")
            student_index = int(stdscr.getstr().decode()) - 1
            stdscr.addstr("Enter Course ID to enter mark for the student: ")
            course_id = stdscr.getstr().decode()
            stdscr.addstr("Enter Mark for the student: ")
            mark = float(stdscr.getstr().decode())
            school_listing.students[student_index].input_mark(course_id, mark)
        elif option == 4:
            school_listing.list_students()
            stdscr.getch()  # Wait for key press before clearing the screen
        elif option == 5:
            school_listing.list_courses()
            stdscr.getch()  # Wait for key press before clearing the screen
        else:
            stdscr.addstr("Invalid input. Please try again!\n")
            stdscr.getch()  # Wait for key press before clearing the screen

    curses.endwin()


if __name__ == "__main__":
    curses.wrapper(main)
