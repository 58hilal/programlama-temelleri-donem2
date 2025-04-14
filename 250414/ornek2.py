saat_sure=int(input("kaç dakika kalacaksa"))
if saat_sure<=60:
    print("ücret:5 tl")
elif saat_sure<=300:
    print("ücret",(saat_sure/60)*4)
else:
    print("ücret",(saat_sure/60)*3)
    