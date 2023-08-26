l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

s1 = set(l1)
s2 = set(l2)

s3 = s1.intersection(s2)
print("Elementos comunes:",s3)

s4 = s1.symmetric_difference(s2)
print("Elementos unicos son:",s4)

l3 = sorted(list(s3) + list(s4), key=lambda x: x[1]) # utilizamos el key para toma un elemento de la lista y devuelve un valor que se utiliza para comparar y ordenar los elementos.
# key=lambda x: x[1]: Estamos indicando como ordenar la lista de tuplas basándote en los valores numéricos de la posición 1 de cada tupla.
print(l3)