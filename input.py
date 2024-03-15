def get_student_input(stdscr):
    stdscr.addstr("Enter Student ID: ")
    student_id = stdscr.getstr().decode()
    stdscr.addstr("Enter Student Name: ")
    student_name = stdscr.getstr().decode()
    stdscr.addstr("Enter Student Date of Birth (DoB): ")
    dob = stdscr.getstr().decode()
    return student_id, student_name, dob

def get_course_input(stdscr):
    stdscr.addstr("Enter Course ID: ")
    course_id = stdscr.getstr().decode()
    stdscr.addstr("Enter Course Name: ")
    course_name = stdscr.getstr().decode()
    return course_id, course_name

def get_mark_input(stdscr):
    stdscr.addstr("Enter student index to enter mark: ")
    student_index = int(stdscr.getstr().decode()) - 1
    stdscr.addstr("Enter Course ID to enter mark for the student: ")
    course_id = stdscr.getstr().decode()
    stdscr.addstr("Enter Mark for the student: ")
    mark = float(stdscr.getstr().decode())
    return student_index, course_id, mark
