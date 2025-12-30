#Guessing Game
#Game picks random number between 1&10
import random
num = random.randint(1,10)
guess = None
guess_count = 0
#until guess matches num they will be asked to reenter guess
while guess != num:
    try:
        guess= int(input('Enter number between 1 & 10: '))
        guess_count += 1
        if guess < 1 or guess > 10:
            print('Number out of range! Try again.')
            continue
        if guess < num: 
            print('Higher')
            print(guess)
        elif guess > num: 
            print('Lower')
            print (guess)
        if guess == num: 
            print('Correct! You Win!')
            break
    except:
        raise ValueError('Not a number')
print('Total guesses: ' + str(guess_count))        
