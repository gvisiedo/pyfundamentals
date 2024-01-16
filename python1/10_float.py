from tkinter import Y


x = 3.3
y = 1.1 + 2.2

print(y)
print(x)

print(x == y)

y_string = format(y, ".2g")
print(y_string)

print(y_string == str(x))

print('*' * 10)

print(y,x)


tolerance = 0.00001

print(abs(x - y )< tolerance)

