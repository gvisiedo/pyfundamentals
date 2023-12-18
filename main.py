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

user_option = input('Piedra, papel o tijera => ')
computer_option = 'piedra'

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




