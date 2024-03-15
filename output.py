def display_student_list(stdscr, students):
    if not students:
        stdscr.addstr("There aren't any students!\n")
    else:
        stdscr.addstr("Student List:\n")
        for i, student in enumerate(students):
            stdscr.addstr(f"{i + 1}. ID: {student.get_id()} - Name: {student.get_name()} - DoB: {student.get_dob()}\n")
            if student.get_marks():
                stdscr.addstr("   Marks (Course Id - Mark): {}\n".format(student.get_marks()))

def display_course_list(stdscr, courses):
    if not courses:
        stdscr.addstr("There aren't any courses!\n")
    else:
        stdscr.addstr("Course List:\n")
        for i, course in enumerate(courses):
            stdscr.addstr(f"{i + 1}. ID: {course.id} - Name: {course.name}\n")
