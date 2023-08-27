while True:
    try:
        a = float(input('Ingrese un número que desee hallar: '))
        b = float(input('Ingrese un número que desee hallar: '))
        signo = input("Ingrese un signo para realizar la operación (+, -, *, /): ")

        if signo == '+':
            respuesta = a + b
        elif signo == '-':
                respuesta = a - b
        elif signo == '*':
                respuesta = a * b
        elif signo == '/':
            if b != 0:  # Agregamos una verificación para evitar la división por cero
                respuesta = a / b
            else:
                respuesta = "Error en la división por cero"
        else:
            respuesta = "Debe ingresar un signo válido (+, -, *, /)"
        
        print("El resultado es:", respuesta)

    except ValueError:
        print("Error: Ingresa números válidos.")
    except ZeroDivisionError as e:
        print(e)