import math

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
