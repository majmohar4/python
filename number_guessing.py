import random
a = 20

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
        #veckratnik
        if izbiranamiga == 1:
            večkratnik = stevilka * stevilo1
            print("Večkratnik tega števila je" + str(večkratnik))
        
        elif izbiranamiga == 2:
            if a >= 1:
                if poskus % a == 0:
                    print("Delitelj tega števila je "+ str((a)))
                else :
                    a = a - 1
