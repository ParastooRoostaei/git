class Bmi:

    def __init__(self, weight, height):
        self.set_weight(weight)
        self.set_height(height)

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight():
        return self.__weight

    def set_height(self, height):
        self.__height = height

    def get_height():
        return self.__height

    def calculate_bmi(self):
        return self.__weight / ((self.__height **2) /10000)
    
    def check_bmi(self, a):
        if a < 18.5:
            p = "you are lean"
        elif 18.5 < a and a < 24.9:
            p = "your weight is natural"
        elif 25 < a and a < 29.9 :
            p = "you overweighted"
        elif a >30 :
            p = "obese"
        return p


w = int(input("enter your weight:"))
h = int(input("enter your height:"))

bmi1 = Bmi(w, h)

result = bmi1.calculate_bmi()

print(bmi1.check_bmi(result))