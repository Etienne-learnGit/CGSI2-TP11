class complex :

    def __init__(self, Re, Im):
        self.__Re = Re
        self.__Im = Im

    def __add__(self, obj):
        return complex(self.__Re+obj.__Re, self.__Im+obj.__Im)

    def __sub__(self, obj):
        return complex(self.__Re-obj.__Re, self.__Im-obj.__Im)

    def __mul__(self, obj):
        a = self.__Re
        b = self.__Im
        A = obj.__Re
        B = obj.__Im
        return complex(a*A-B*b, a*B+b*A)

    def __truediv__(self, obj):
        a = self.__Re
        b = self.__Im
        A = obj.__Re
        B = obj.__Im
        return complex((a*A+b*B)/(A**2-B**2),(a*B+b*A)/(A**2-B**2))

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
    print(c9)
