kilo= int(input("kg giriniz :"))
if kilo<=10:
    ucret=10*kilo
    print("odenecek tutar:",ucret)
else:
    ucret=100+(kilo-10)* 7.5
    print("odencek tutar",ucret)