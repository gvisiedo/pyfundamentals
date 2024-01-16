name = "Nico"
last_name = "Molon"

full_name = name + last_name

print(full_name)

full_name = name + " " + last_name

print(full_name)

quote = "I'm Nico"

print(quote)

quote2 = ' She said "Hello" '

print(quote2)

#format

template = "Hola, mi nombre es " + name + "y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)