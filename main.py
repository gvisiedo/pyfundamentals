import random

print("Hello World")
# Comentarios de una linea
#print(12 * 5)

print(5 + 5)

'''
Comentario de varias lineas
'''

print("hola")
print("hola")
print("Hola gramola")

options=('piedra','papel', 'tijera')

user_option = input('piedra, papel o tijera => ')
user_option=user_option.lower()
if not user_option in options:
    print('esa opción no es valida')
computer_option = random.choise(options)

print('User option =>', user_option)
print('Computer option =>', computer_option)

if user_option == computer_option:
    print('Empate')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('user gano!')
    else:
        print('Papel gana a piedra')
        print('computer gano!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a piedra')
        print('user gana')
    else:
        print('tijera gana a papel')
        print('computer gano!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('user gano!')
    else:
        print('print gana a tijera')
        print('computer gana')




