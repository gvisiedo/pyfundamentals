from ast import If


if True:
    print('deberia ejecutarse')

if False:
    print('nunca se ejecuta')





pet = input('Cual es tu mascota favorita? ')

if pet == 'perro':
    print('genial tienes buen gusto')

if pet == 'gato':
    print('espero tengas suerte')


if pet == 'pez':
    print('eres lo maximo')


stock = int(input('Digita l stock => '))

if stock >= 100 and stock <=1000:
    print('el sock es correct')
else:
    print('El stock es incorrecto')

if pet == 'perro':
    print('genial')
elif pet == 'gato':
    print('ten suerte')
elif pet == 'pez':
    print('lo maximo')
else:
    print('te falta una mascota')

number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
    print('es par')
else:
    print('Es impar')



