import curses
from input import get_student_input, get_course_input, get_mark_input
from output import display_student_list, display_course_list
from domains.student import Student
from domains.course import Course

class Listing:
    def __init__(self):
        self.students = []
        self.courses = []

    def list_students(self, stdscr):
        display_student_list(stdscr, self.students)

    def list_courses(self, stdscr):
        display_course_list(stdscr, self.courses)

    def add_student(self, student_id, student_name, dob):
        student = Student(student_id, student_name, dob)
        self.students.append(student)

    def add_course(self, course_id, course_name):
        course = Course(course_id, course_name)
        self.courses.append(course)

    def input_mark(self, student_index, course_id, mark):
        self.students[student_index].input_mark(course_id, mark)

    def main(self, stdscr):
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
                # Add Student
                student_id, student_name, dob = get_student_input(stdscr)
                self.add_student(student_id, student_name, dob)
            elif option == 2:
                # Add Course
                course_id, course_name = get_course_input(stdscr)
                self.add_course(course_id, course_name)
            elif option == 3:
                # Input Mark for Student
                student_index, course_id, mark = get_mark_input(stdscr)
                self.input_mark(student_index, course_id, mark)
            elif option == 4:
                # List Students
                self.list_students(stdscr)
                stdscr.getch()  # Wait for key press before clearing the screen
            elif option == 5:
                # List Courses
                self.list_courses(stdscr)
                stdscr.getch()  # Wait for key press before clearing the screen
            else:
                stdscr.addstr("Invalid input. Please try again!\n")
                stdscr.getch()  # Wait for key press before clearing the screen

        curses.endwin()

if __name__ == "__main__":
    curses.wrapper(Listing().main)
