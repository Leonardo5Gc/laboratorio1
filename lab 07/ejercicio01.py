persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

#A SOLUCION

if 'skills' in persona:
    habilidades = persona['skills']
    if len(habilidades) >= 3:
        habilidad_media = habilidades[len(habilidades) // 2]
        print("Habilidad del medio:", habilidad_media)

# B SOLUCION

if 'skills' in persona:
    habilidades = persona['skills']
    if 'Python' in habilidades:
        print("La persona tiene habilidad en Python.")

# C SOLUCION

if 'skills' in persona:
    skills = persona['skills']
    if skills[1 and 2] == ['JavaScript', 'React']:
        print("Él es un desarrollador frontend")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("Él es un desarrollador backend")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("Él es un desarrollador fullstack")
    else:
        print("Título desconocido")
