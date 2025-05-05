toplam=0
liste=[]

for i in range(5):
    liste.append(int(input("bir sayı girin:")))

    for sayi in liste:
        toplam = toplam + sayi
        if toplam % 2==0:
            print("sayıları toplamı çifttir")
        else:
            print("sayıların toplamı tektir")