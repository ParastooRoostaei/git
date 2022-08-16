class Chegali:

    def __init__(self, jerm, hajm):
        self.__jerm = jerm
        self.__hajm = hajm

    @property
    def jerm(self):
        return self.__jerm

    @jerm.setter
    def jerm(self, jerm):
        if jerm < 0 :
            self.__jerm = jerm * (-1)
        else:
            self.__jerm = jerm

    @property
    def hajm(self):
        return self.__hajm

    @hajm.setter
    def hajm(self, hajm):
        self.__hajm = hajm

    def chegali(self):
        return (self.__jerm / self.__hajm)

jerm1 = float(input("Enter jerm:"))
hajm1 = float(input("Enter hajm:"))

ch1 = Chegali(jerm1, hajm1)

print(ch1.chegali())