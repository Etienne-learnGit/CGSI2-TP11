class rational:

    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __add__(self, obj):
        if isinstance(obj, rational) :
            return rational( self.__num*obj.__den+obj.__num*self.__den , self.__den*obj.__den)

    def __sub__(self, obj):
        if isinstance(obj, rational) :
            return rational( self.__num*obj.__den-obj.__num*self.__den , self.__den*obj.__den)

    def __mul__(self, obj):
        if isinstance(obj, rational) :
            return rational(self.__num*obj.__num, self.__den*obj.__den)

    def __truediv__(self, obj):
        if isinstance(obj, rational) :
            return rational(self.__num*obj.__den, self.__den*obj.__num)

    def __abs__(self):
        return rational( ((self.__num)**2)*(1/2), ((self.__den)**2)*(1/2) )

    def __eq__(self, obj):
        if isinstance(obj, rational) :
            return self.__num/self.__den == obj.__num*obj.__den

    def __ne__(self, obj):
        if isinstance(obj, rational) :
            return self.__num/self.__den != obj.__num*obj.__den

    def __str__(self):
        return ("("+str(self.__num)+"/"+str(self.__den)+")")

if __name__ == '__main__' :
    r1 = rational(8,9)
    r2 = rational(5,4)
    r3 = r1 + r2
    r4 = r2 - r1
    r5 = (r2==r1)
    print(r3)
    print(r5)
