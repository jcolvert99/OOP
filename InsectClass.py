import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight_length = 0


    def flight_length(self):
        self.flight_length = random.randint(1, 10)
        

    def get_miles(self):
        return self.flight_length
            
