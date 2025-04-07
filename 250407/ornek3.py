kadi=input("kullanıcı adını girin :")
karakter_sayi=len(kadi)
if karakter_sayi==0:
    print("KULLANICI ADI BOŞ GEÇİLEMEZ")
elif karakter_sayi>0 and karakter_sayi<9:
    print("KULLANICI ADI ÇOK KISA")
elif karakter_sayi>=0 and karakter_sayi<=0:
    print("kullanıcı adı uygun")
else:
    print("kullanıcı adı uzun")