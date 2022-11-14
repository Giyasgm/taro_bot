class Formules:

    def __init__(self, spis):
        self.spis = spis
        self.spisok = []

    def razbor(self):
        s = self.spis.split('.')
        for i in s:
            self.spisok.append(int(i))

    def day(self):
        self.razbor()
        arkan = 0
        while self.spisok[0] != 0:
            b = self.spisok[0] % 10
            arkan += b
            self.spisok[0] = self.spisok[0] // 10
        return arkan

    def month(self):
        self.razbor()
        arkan = 0
        while self.spisok[1] != 0:
            b = self.spisok[1] % 10
            arkan += b
            self.spisok[1] = self.spisok[1] // 10
        return arkan

    def year(self):
        self.razbor()
        arkan = 0
        while self.spisok[2] != 0:
            b = self.spisok[2] % 10
            arkan += b
            self.spisok[2] = self.spisok[2] // 10
        if arkan > 21:
            newark = 0
            while arkan != 0:
                b = arkan % 10
                newark += b
                arkan = arkan // 10
            return newark
        else:
            return arkan

    def alldata(self):
        summa = self.day() + self.month() + self.year()
        if summa > 21:
            allark = 0
            while summa != 0:
                b = summa % 10
                allark += b
                summa = summa // 10
            return allark
        else:
            return summa
