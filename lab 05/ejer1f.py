edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
valorMin = min(edades)
valorMax = max(edades)
promedio = (sum(edades) / len(edades))
resultA = (valorMin - promedio), abs(valorMin - promedio)
resultB = (valorMax - promedio), abs(valorMax - promedio) 

print(resultA)
print(resultB)