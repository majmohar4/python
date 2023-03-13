#vpraša me a bi rad vadu seštevat/odštevat/množit/delit
#vpraša me kolik računov bi rad
#šteje točke
#na koncu displaya rezultat
#in v procentih


import random

operacija=input("Vpiši 1 za seštevanje, 2 za odštevanje, 3 za množenj in 4 za deljenje.")
steviloracunov=input("Koliko računov želiš?")
tocke = 0
procenti = 0
while steviloracunov != 0:
    if operacija == 1:
        stevilka1=random.randint(1, 10)
        stevilka2=random.randint(1, 10)
        racun = input("Koliko je ", stevilka1, " x ", stevilka2, "?")

        steviloracunov= steviloracunov -1

        if racun== (stevilka1*stevilka2):
            print("Odgovor je pravilen.")
            tocke = tocke + 1
        else :
            print("Odgovor je nepravilen")





stevilkica=random.randint(1, 9)
print(stevilkica)