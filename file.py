
file=open("dorian.txt", "r+")

besedilo=file.read()

"""""
poskus = str(input("vpiši geslo"))
if poskus == geslo:
    print("geslo je pravilno")
"""""


if "1234" in besedilo:
    print("našel sem")