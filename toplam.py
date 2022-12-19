sayi1=int(input("Sayı 1: "))
sayi2=int(input("Sayı 2: "))

print("Hangi işlemi yapmak istiyorsunuz (+,-,*,/): ")
islem = input()
if islem == '+':
    print("\n" +str(sayi1)+ " + " +str(sayi2)+ " = " +str(sayi1+sayi2))
elif islem == '-':
    print("\n" +str(sayi1)+ " - " +str(sayi2)+ " = " +str(sayi1-sayi2))
elif islem == '*':
    print("\n" +str(sayi1)+ " * " +str(sayi2)+ " = " +str(sayi1*sayi2))
elif islem == '/':
    print("\n" +str(sayi1)+ " / " +str(sayi2)+ " = " +str(sayi1/sayi2))
else:
    print("\nBöyle bir işlem bulunmuyor.")
