import random

stevilka = random.randint(1, 100)
poskus = int(input("Ugani številko med 1 in 100: "))
poskusi = int(input("Vnesi število poskusov, ki jih želiš imeti."))
tocke = 10
a = 0

if poskusi != 0:
    poskus = int(input("Vnesi tvoj naslednji poskus."))
    while poskus != stevilka:
        print("Številka ni prava.")
        izbiranamiga = random.randint(1, 5)
        stevilo1 = random.randint(1, 5)
        if izbiranamiga == 1:
            večkratnik = stevilka * stevilo1
            print("Večkratnik tega števila je" + večkratnik)
        elif izbiranamiga == 2:
            while a >= 1:
                stevilo2 = stevilo2 + 1
                količnik = stevilka // stevilo2