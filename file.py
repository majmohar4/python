
file=open("dorian.txt", "a")

file.write("Doriana ni v šoli.\n")


file=open("dorian.txt", "r")
dorian = str(file.read())
print(dorian[0:6])

