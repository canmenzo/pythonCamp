sehirler = ["Ankara", "Istanbul", "Izmir"]

# for sehir in sehirler:
#     print(sehir)

# # for sayi in range(0, 10, 2):
# #     print(sayi)

# sayac = 1
# while sayac<=10:
#     print(sayac)
#     sayac = sayac + 1

# isim = input("Adiniz")
# print("isim: "+isim)

sayi = int(input("faktroiyeli hesaplanicak sayi : "))
faktoriyel = 1

if sayi<0:
    print("Negatif sayilarin faktoriyeli hesaplanmaz")
elif sayi==0:
    print("Sonuc: 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
    print("Sonuc: ", faktoriyel)

