class matrice :

    def __init__(self, data):
        self.__data = data

    def __str__(self):
        return ("["+str(self.__data[0][0])+"  "+str(self.__data[0][1])+"\n "+str(self.__data[1][0])+"  "+str(self.__data[1][1])+"]")

    def __add__(self, obj):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]+obj.__data[0][0])
        lst1.append(self.__data[0][1]+obj.__data[0][1])
        lst2.append(self.__data[1][0]+obj.__data[1][0])
        lst2.append(self.__data[1][1]+obj.__data[1][1])
        return matrice([lst1,lst2])

    def __sub__(self, obj):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]-obj.__data[0][0])
        lst1.append(self.__data[0][1]-obj.__data[0][1])
        lst2.append(self.__data[1][0]-obj.__data[1][0])
        lst2.append(self.__data[1][1]-obj.__data[1][1])
        return matrice([lst1,lst2])


    def __iadd__(self, obj):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]+obj.__data[0][0])
        lst1.append(self.__data[0][1]+obj.__data[0][1])
        lst2.append(self.__data[1][0]+obj.__data[1][0])
        lst2.append(self.__data[1][1]+obj.__data[1][1])
        self.__data[0] = lst1
        self.__data[1] = lst2
        return matrice(self.__data)


    def __isub__(self, obj):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]-obj.__data[0][0])
        lst1.append(self.__data[0][1]-obj.__data[0][1])
        lst2.append(self.__data[1][0]-obj.__data[1][0])
        lst2.append(self.__data[1][1]-obj.__data[1][1])
        self.__data[0] = lst1
        self.__data[1] = lst2
        return matrice(self.__data)

    def __mul__(self, obj):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]*obj.__data[0][0]+self.__data[0][1]*obj.__data[1][0])
        lst1.append(self.__data[0][0]*obj.__data[0][1]+self.__data[0][1]*obj.__data[1][1])
        lst2.append(self.__data[1][0]*obj.__data[0][0]+self.__data[1][1]*obj.__data[1][0])
        lst2.append(self.__data[1][0]*obj.__data[0][1]+self.__data[1][1]*obj.__data[1][1])
        return matrice([lst1, lst2])

    def __imul__(self, obj):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]*obj.__data[0][0]+self.__data[0][1]*obj.__data[1][0])
        lst1.append(self.__data[0][0]*obj.__data[0][1]+self.__data[0][1]*obj.__data[1][1])
        lst2.append(self.__data[1][0]*obj.__data[0][0]+self.__data[1][1]*obj.__data[1][0])
        lst2.append(self.__data[1][0]*obj.__data[0][1]+self.__data[1][1]*obj.__data[1][1])
        self.__data[0] = lst1
        self.__data[1] = lst2
        return matrice(self.__data)

if __name__ == '__main__' :
    m1 = matrice([[1,0],[0,1]])
    m2 = matrice([[2,1],[1,0]])
    m3 = m1 + m2
    m2 += m1
    m5 = m1 * m3
    print(m5)
