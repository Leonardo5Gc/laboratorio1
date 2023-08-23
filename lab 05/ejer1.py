edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
print("El orden correcto vendria ser: ",edades)
edadMin = min(edades)
edadMax = max(edades)
edades.insert(0, edadMin)
edades.insert(0, edadMax) 

print(edades)

