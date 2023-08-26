lista1 = list(range(1,11))
lista2 = list(range(5,16))
lista3 = list(range(10,21))

conj1 = set(lista1)
conj2 = set(lista2)
conj3 = set(lista3)

conjunto_comun = conj1.intersection(conj2 and conj3)
print('El conjunto en comun de los 3 es:',conjunto_comun)

conjunto_presentes = conj1.union(conj2 and conj3)
print('Los conjuntos presentes son:',conjunto_presentes)

presente_primera = (conj1-conj3)
print('Solo presente en la primera lista',presente_primera)

tupla1 = tuple(conjunto_comun)
tupla2 = tuple(conjunto_presentes)
tupla3 = tuple(presente_primera)

print('Las sumas de cada conjunto son:',{max(tupla1) + min(tupla1)},{max(tupla2) + min(tupla2)},{max(tupla3) + min(tupla3)})
