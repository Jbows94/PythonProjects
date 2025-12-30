#Guessing Game
#Game picks random number between 1&10
import random
num = random.randint(1,10)

#until guess matches num they will be asked to reenter guess
try:
    while guess != True
        guess= int(input('Enter number between 1 & 10: '))
        if guess < num: 
            print('Higher')
            print('Enter new guess' + guess)
        elif guess > num: 
            print('Lower')
            print (guess)
    if guess == num: 
        print('Correct! You Win!')
except TypeError:
    print('Error. Enter a number 1-10')
