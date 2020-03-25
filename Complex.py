class complex :

    def __init__(self, Re, Im):
        self.__Re = Re
        self.__Im = Im

    def __add__(self, obj):
        return complex(self.__Re+obj.__Re, self.__Im+obj.__Im)

    def __sub__(self, obj):
        return complex(self.__Re-obj.__Re, self.__Im-obj.__Im)

    def __mul__(self, obj):
        return complex(self.__Re*obj.__Re-obj.__Im*self.__Im, self.__Re*obj.__Im+self.__Im*obj.__Re)

    def __truediv__(self, obj):
        return complex((self.__Re*obj.__Re+self.__Im*obj.__Im)/(obj.__Re**2-obj.__Im**2),(self.__Re*obj.__Im+self.__Im*obj.__Re)/(obj.__Re**2-obj.__Im**2))

    def __abs__(self):
        return complex(int(((self.__Re)**2)**(1/2)), int(((self.__Im)**2)**(1/2)))

    def __eq__(self, obj):
        return self.__Re==obj.__Re and self.__Im==obj.__Im

    def __ne__(self, obj):
        return self.__Re!=obj.__Re or self.__Im!=obj.__Im

    def __str__(self):
        return ("("+str(self.__Re)+","+str(self.__Im)+")")

if __name__ == '__main__' :
    c1 = complex(2,-4)
    c2 = complex(1,3)
    c3 = complex(1,3)
    c4 = c1+c2
    c5 = c1-c2
    c6 = c1*c2
    c7 = c2/c1
    c8 = abs(c1)
    c9 = (c2==c3)
    c10 = (c2!=c1)
    print(c5)
