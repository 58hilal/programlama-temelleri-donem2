sayilar1=[10,11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]

sayilar1.extend(sayilar2)
print(sayilar1)
for sayi in sayilar1:
    if sayi % 4 == 0:
        print(sayi)