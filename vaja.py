a=int(input("Vnesi prvo število."))
b=int(input("Vnesi drugo število."))
ostanek=a%b
zadnji = 0

while ostanek!=0:
	zadnji=ostanek
	
	ostanek=a%b

	a, b = b, ostanek


	print(ostanek, "ostanek")

print(zadnji, "zadnji ostanek")