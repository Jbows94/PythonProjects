#define functions
import functions

print('Welcome to Simple Calc')
name = input('What is your name? ')
functions.say_greet(name)
use_calc = input('Would you like to use the calculator today? Y/N: ')

while use_calc.lower() == 'y':
   try: 
    #declare x and y values
        x= int(input('X= ? '))
        y= int(input('Y= ? '))

    #print all four operations
        print('Sum: ', functions.add(x, y))
        print('Difference: ', functions.diff(x, y))
        print('Multiplied: ', functions.multiply(x, y))
        print('Divided: ', functions.div(x, y))
        new_entry = input('Do you want to continue?: Y/N: ')
        if new_entry.lower() != 'y':
            break
   except ValueError:
       print('Error. Wrong data type.')
print('Thank you for using Simple Calc!')
