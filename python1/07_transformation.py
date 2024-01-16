from unicodedata import name


name = "Nico"

print(type(name))

name = 12

print(type(name))

name = True
print(type(name))

print("Nico" + " Molina")
print(10 + 20)

age = 12

print("Mi edad es " + str(age))

print(f"Mi edad es {age}")

age = input('Escribe tu edad =>')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad es 10 años será {age}')
