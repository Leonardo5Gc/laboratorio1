
text = input("Ingrese un texto de su preferencia ya se en mayuscula o en minuscula: ")

if text.isupper():  #isupper = mayuscula y isupper = trabaja con el primer caracter, es decir, ve si todos son mayus o minus y
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc = "abcdefghijklmnñopqrstuvwxyz"

desplaza = int(input("Ingrese un numero de desplazamiento: ")) #Aqui definimos el valor de desplazamiento

cifrado = "" 
# Realizamos el cifrado
for c in text:
    if c in abc:
        cifrado += abc[(abc.index(c) + desplaza) % len(abc)]
    else:
        cifrado += c

print(cifrado)
