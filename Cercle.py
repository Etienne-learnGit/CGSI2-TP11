class circle :

    def __init__(self, r):
        self.__r = r

    def __add__(self, obj):
        if isinstance(obj, circle) :
            return circle(self.__r+obj.__r)

    def __lt__(self, obj):
        if isinstance(obj, circle) :
            return self.__r < obj.__r

    def __gt__(self, obj):
        if isinstance(obj, circle) :
            return self.__r > obj.__r

    def __str__(self):
        return ("(r = "+str(self.__r)+")")

if __name__ == '__main__' :
    c1 = circle(2)
    c2 = circle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c5)
