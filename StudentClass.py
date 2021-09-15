class Student:
    def __init__(self, StudentID, Name, DateofBirth, classification):
        self.__studentid = StudentID
        self.__name = Name
        self.__dob = DateofBirth
        self.__classifcation = classification

    def calc_age(self, DateofBirth):
