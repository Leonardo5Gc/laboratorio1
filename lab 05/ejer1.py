edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
print("El orden correcto vendria ser: ",edades)
edadMin = min(edades)
edadMax = max(edades)
print('Le edad minima es:',edadMin,'y la edad macima es:',edadMax)
edades.insert(0, edadMin)
edades.insert(0, edadMax) 

print('La edad minima y maxima fue añadida:',edades)

terMedio = (edades[4],  edades[5])
primerele, segundoele = terMedio
result = (primerele + segundoele)/2
print('La edad mediana es:',result)

suma = sum(edades)
numlista = len(edades)
promedio = (suma / numlista)
print('La edad promedio es',promedio)

numMax = max(edades)
numMin = min(edades)
rango = numMax - numMin
print("El rango es de:",rango)

valorMin = min(edades)
valorMax = max(edades)
promedio = (sum(edades) / len(edades))
resultA = (valorMin - promedio), abs(valorMin - promedio)
resultB = (valorMax - promedio), abs(valorMax - promedio) 
print('Comparaion del primer resultado:',resultA)
print('Comparaion del segundo resultado:',resultB)