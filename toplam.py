sayi1=int(input("Sayı 1: "))
sayi2=int(input("Sayı 2: "))
toplam=sayi1+sayi2
print("Toplam: ",toplam)
def palindrom(toplam):
    res = [int(x) for x in str(toplam)]
    res2 = [int(x) for x in str(toplam)]
    res.reverse()
    if res == res2:
        print("Sayı Palindrom")
    else:
        print("Sayı Palindrom Değil")
def basamaktoplam(toplam):
    bas = [int(x) for x in str(toplam)]
    print("Sayının Basamakları Toplamı", sum(bas))

palindrom(toplam)
basamaktoplam(toplam)
