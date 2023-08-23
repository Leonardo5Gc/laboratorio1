entrada = input("Ingrese una palabra: ")
polin = entrada[::-1]
if entrada == polin:
    print(True)
else:
    print(False)