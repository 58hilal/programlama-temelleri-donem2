sayi1=input("bir sayı giriniz:")
sayi2=input("bir sayı giriniz:")
islem=input("işlem seçin(+,-,*,\)")
if islem =="+" :
    sonuc=sayi1+sayi2
    print(sonuc)
elif islem =="-" :
    sonuc=sayi1-sayi2
    print(sonuc)
elif islem =="*" :
    sonuc=sayi1*sayi2
    print(sonuc)
elif  islem =="/" :
    sonuc=sayi1/sayi2
    print(sonuc)
else:
    print("yanlış işlem girdiniz")
