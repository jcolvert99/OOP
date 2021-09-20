from datetime import date


class Student:
    def __init__(self, StudentID, Name, DateofBirth, classification):
        self.__studentid = StudentID
        self.__name = Name
        self.__dob = DateofBirth
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    def calc_age(self):
        today = date.today()
        bday = self.__dob.split('/')
        bday_year = int(bday[2])
        age = today.year - bday_year
        self.__age = age

    def registration_dates(self):
        if self.__classification == 'Seniors':
            self.__register = '11/1 - 11/3'
        elif self.__classification == 'Juniors':
            self.__register = '11/4 - 11/6'
        elif self.__classification == 'Sophomores':
            self.__register = '11/7 - 11/9'
        elif self.__classification == 'Freshman':
            self.__register = '11/10 - 11/12'
        else:
            self.__register = 'Classification not found'

    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.__register
