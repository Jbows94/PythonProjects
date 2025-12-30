#define functions
def add(a, b):
    return a + b
def diff(a, b):
    return a - b
def multiply(a, b):
    return a * b
def div(a, b):
    return a / b


#declare x and y values
x= int(input('X= ? '))
y= int(input('Y= ? '))

#print all four operations
print('Sum: ', add(x, y))
print('Difference: ', diff(x, y))
print('Multiplied: ', multiply(x, y))
print('Divided: ', div(x, y))
