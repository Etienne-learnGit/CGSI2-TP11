class duree :
    def __init__(self, H, M, S): #heures, minutes, secondes
        self.__H = H
        self.__M = M
        self.__S = S

    def __str__(self):
        return (str(self.__H)+"h"+str(self.__M)+"m"+str(self.__S)+"s")

    def __add__(self, obj):
        heure = self.__H+obj.__H
        minute = self.__M+obj.__M
        seconde = self.__S+obj.__S
        while seconde >= 60 :
            minute += 1
            seconde -= 60
        while minute >= 60 :
            heure += 1
            minute -= 60
        return duree(heure, minute, seconde)

if __name__ == '__main__' :
    d1 = duree(1, 59, 20)
    d2 = duree(0, 2, 40)
    d3 = duree(2, 20, 48)
    d4 = d1 + d2
    print(d4)

