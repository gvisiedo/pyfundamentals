text = 'Ella sabe programar en Python'
print('Javascript' in text)
print('Python' in text)

if 'Python' in text:
    print('Eligiste bien!!')
else:
    print('También digiste bien')

size = len(text)
print(size)

print(text) 
print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())



