class Bmi2:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def calculatr_bmi(self):
        return self.__weight / ((self.__height ** 2) / 10000)

    def check_bmi(self, a):
        if a < 18.5 :
            p = "you are lean."
        elif a > 18.5 and a < 24.9:
            p = "your weight is natural."
        elif a > 25 and a < 29.9:
            p = "you overweighted."
        elif a > 30:
            p = "obese."
        
        return p

w = int(input("Enter your weight:"))
h = int(input("Enter your height:"))

bmi1 = Bmi2(w,h)

result = bmi1.calculatr_bmi()
print(bmi1.check_bmi(result))