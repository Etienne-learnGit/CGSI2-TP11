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

    def
