class My_Circle:

    pi = 3.14

    def __init__(self, round):
        self.set_round(round)

    def set_round(self, round):
        if round < 0:
            self.__round = round * (-1)
        else:
            self.__round = round

    def get_round(self):
        return self.__round

    def ghotr(self):
        return 2 * self.__round

    def mohit(self):
        return 2 * self.pi * self.__round
    
    def masahat(self):
        return self.pi * self.__round ** 2


r = float(input("Enter round:"))
circle1 = My_Circle(r)
print(circle1.ghotr())
print(circle1.mohit())
print(circle1.masahat())