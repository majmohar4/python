import random

def večkratnik(stevilo):
    stevilo1 = random.randint(1, 5)
    večkratnik = stevilo * stevilo1
def delitelj(stevilka, a):
    while a > 1:
                if poskus % a == 0:
                    print("Delitelj tega števila je "+ str((a)))
                else :
                    a = a - 1
    if a == 0:
         print("To število, ki ga iščeš nima deljitelja, razen 1.")
def primerjava(poskus, stevilo):
     if poskus <= stevilka:
          print("Tvoj poskus je bil premajhen.")
     elif poskus >= stevilka:
          print("Tvoj poskus je bil previsok.")
def namig():
     print("Dobil si namig:")


stevilka = random.randint(1, 100)
poskusi = int(input("Vnesi število poskusov, ki jih želiš imeti."))
poskus = int(input("Ugani številko med 1 in 100: "))
vsiposkusi = poskusi
točke = 0
možnetočke = 10
a = 0
index=1
vsiposkusi = poskusi

while poskusi != 0:
    if vsiposkusi != poskusi or index!=1:
        
        poskus = int(input("Vnesi tvoj naslednji poskus."))
    if vsiposkusi >= poskusi:
        if poskus != stevilka:
            izbiranamiga = random.randint(1, 4)
            print("Številka ni prava.")
            namig2 = str(input("Ali želiš namig?"))
            namig2 = namig2.lower()
            if (namig2 == "ja"):
                možnetočke = možnetočke - 1
                #veckratnik
                if izbiranamiga == 1:
                    večkratnik(stevilka)
                    namig()
                    print("Večkratnik tega števila je" + str(večkratnik))
                elif izbiranamiga == 2:
                    namig()
                    delitelj(stevilka, a)
                elif izbiranamiga == 3:
                    namig()
                    primerjava(poskus, stevilka)
                elif izbiranamiga == 4:
                    namig()
                    večkratnik(stevilka)
                    delitelj(stevilka, a)
                    primerjava(poskus, stevilka)
                poskusi = poskusi - 1
                index+=1
                if poskusi != 0:
                    print("Poskusi še enkrat!")

if vsiposkusi == poskusi:
     print("Bravo! Uganil si v prvem poiskusu.")
točke = točke + možnetočke
print("Dobil si " + točke)
print("Nisi uganil števila.")