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
lista = []
for habilidades in persona['skills']:
    lista.append(habilidades)
print("Las siguientes habilidades lo conforma:",lista)
#

for valor in persona['skills']:
    if valor == ('Python'):
        print('El valor que se obtuvo fue:',"'",valor,"'")
'''
if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad 'Python'.")
    '''
#
'''
for valor in persona['skills']:
    if valor == 'JavaScript' and valor == 'React':
        print('los unicos valores son:', lon(1 and 2))
'''
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