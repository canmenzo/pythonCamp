class Matematik:
    def __init__(self, sayi1, sayi2): #constructor / yapici blok
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik basladi(referansi olustu)")
    def topla(self):
        return self.s1 + self.s2
    def cikar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2

matematik = Matematik(14, 7)
sonuc = matematik.bol()
print("Sonuc : " + str(sonuc))


class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        self.s1 = sayi1
        self.s2 = sayi2
    def varyansHesapla(self):
        return self.s1 * self.s2

##inheritance calismalarini incele

istatistik = Istatistik(5,8)
sonuc2 = istatistik.topla()
print("Sonuc2 : " + str(sonuc2))