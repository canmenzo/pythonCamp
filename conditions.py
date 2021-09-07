istenenKredi = 100000
hesap = 9233
minGerekenHesap = 10000

if hesap>=minGerekenHesap:
    print ("kredi verilebilir")
elif hesap>=9000 and hesap<=9500:
    print("genel mudure sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("mudure sorulacak")
else:
    print ("kredi verilemez")
