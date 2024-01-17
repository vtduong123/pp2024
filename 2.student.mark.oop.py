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