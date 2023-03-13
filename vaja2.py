#vpraša me a bi rad vadu seštevat/odštevat/množit/delit
#vpraša me kolik računov bi rad
#šteje točke
#na koncu displaya rezultat
#in v procentih


import random
pravilne = 0
napacne = 0
operacija=input("Vpiši 1 za seštevanje, 2 za odštevanje in 3 za množenje.")
steviloracunov=int(input("Koliko računov želiš?"))
tocke = 0
procenti = 0
operacija = int(operacija)
steviloracunov2 = steviloracunov
while steviloracunov != 0:
    if operacija == 1:
        stevilka1=random.randint(1, 10)
        stevilka2=random.randint(1, 10)
        racun = int(input("Koliko je "+ str(stevilka1)+ " + "+ str(stevilka2)+ "?"))
        steviloracunov= steviloracunov - 1

        if racun== (stevilka1 + stevilka2):
            print("Odgovor je pravilen.")
            tocke = tocke + 1
            pravilne =pravilne + 1
        else :
            print("Odgovor je nepravilen")
            napacne = napacne + 1
    if operacija == 2:
        stevilka1=random.randint(1, 10)
        stevilka2=random.randint(1, 10)
        racun = int(input("Koliko je "+ str(stevilka1)+ " - "+ str(stevilka2)+ "?"))
        racun = int(racun)
        steviloracunov= steviloracunov -1

        if racun== (stevilka1 - stevilka2):
            print("Odgovor je pravilen.")
            tocke = tocke + 1
            pravilne = pravilne + 1
        else :
            print("Odgovor je nepravilen")
            napacne = napacne + 1
    if operacija == 3:
        stevilka1=random.randint(1, 10)
        stevilka2=random.randint(1, 10)
        racun = int(input("Koliko je "+ str(stevilka1)+ " x "+ str(stevilka2)+ "?"))
        racun = int(racun)
        steviloracunov= steviloracunov -1

        if racun == (stevilka1 * stevilka2):
            print("Odgovor je pravilen.")
            tocke = tocke + 1
            pravilne = pravilne + 1
        else :
            print("Odgovor je nepravilen")
            napacne = napacne + 1

print("Dosegel si ", tocke, " stevilo točk.")
procenti = (pravilne / steviloracunov2) * 100
print("Dosegel si ", procenti, " %.")