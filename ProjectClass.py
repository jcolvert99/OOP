class Project:
    def __init__(self, projid, desc, consultants, duedate):
        self.__projID = projid
        self.__projDesc = desc
        self.__consultants = consultants
        self.__dueDate = duedate

    def get_ID(self):
        return self.__projID

    def get_Desc(self):
        return self.__projDesc

    def get_consultants(self):
        return self.__consultants

    def get_dueDate(self):
        return self.__dueDate
