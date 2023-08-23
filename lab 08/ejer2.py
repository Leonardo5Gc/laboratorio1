import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))    #la función choice() permite elegir aleatoriamente
    return contraseña

if __name__ == "__main__":  # corre ciertas líneas de código si se está ejecutando el programa desde el intérprete
    longitudContra = len(input("Indique su nombre completo para generar una contraseña : "))
    generar = generar_contraseña(longitudContra)
    print("Contraseña generada:", generar)
