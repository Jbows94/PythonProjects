#define functions
import functions

#declare x and y values
x= int(input('X= ? '))
y= int(input('Y= ? '))

#print all four operations
print('Sum: ', functions.add(x, y))
print('Difference: ', functions.diff(x, y))
print('Multiplied: ', functions.multiply(x, y))
print('Divided: ', functions.div(x, y))
