palabra = input("Ingrese una palabra POLINDROMA: ")
polin = palabra[::-1]

print("Su palabra revertida de",palabra ,"es: ",polin)

if palabra == polin:
    print("Es polindroma")
else:
    print("No es polindroma")
