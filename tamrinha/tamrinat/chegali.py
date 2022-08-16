class Chegali:

    def __init__(self, jerm, hajm):
        self.set_hajm(hajm)
        self.set_jerm(jerm)
    
    def set_jerm(self, jerm):
        if jerm < 0 :
            self.__jerm = jerm * (-1)
        else:
            self.__jerm = jerm

    def get_jerm(self):
        return self.__jerm

    def set_hajm(self, hajm):
        self.__hajm = hajm

    def get_hajm(self):
        return self.__hajm

    def chegali(self):
        return (self.__jerm / self.__hajm)

jerm1 = float(input("Enter jerm:"))
hajm1 = float(input("Enter hajm:"))

ch1 = Chegali(jerm1, hajm1)
print(ch1.chegali())