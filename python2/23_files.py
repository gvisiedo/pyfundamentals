file = open('./text.txt')
print(file.read()) #archivo entero
print(file.readline()) #linea a linea

for line in file:
    print(line)

file.close()

with open('./text.txt') as file:
    for line in file:
        print(line)
