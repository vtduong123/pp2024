class Student:
    def __init__(self, student_id, student_name, dob):
        self.__id = student_id
        self.__name = student_name
        self.__DOB = dob
        self.__marks = {}
    
    def input_mark(self, course_id, mark):
        self.__marks[course_id] = mark
          
    def input_id(self, student_id):
        self.__id = student_id
    
    def input_id(self, student_name):
        self.__name = student_name
        
    def input_id(self, dob):
        self.__DOB = dob
        
class course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        
    def input_course(self):
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        return course(course_id, name)
    
class listing:
    def __init__(self):
        self.Student = []
        self.course = []
        
    def list_students(self):
        if not self.Student:
            print("There aren't any students!")
        else:
            print("The list are: ")
            for i, student in enumerate(self.Student):
                print(f"{i+1}. {student.id} - {student.name} - {student.dob}")
                if student.marks:
                    print("Marks (Course Id - Mark): ", student.marks)


def main(self):
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
                self.students.append(self.input_student_info())
            elif option == 2:
                self.courses.append(self.input_course_info())
            elif option == 3:
                self.input_mark()
            elif option == 4:
                self.list_students()
            elif option == 5:
                self.list_courses()
            else:
                print("Invalid input. Please try again!")
