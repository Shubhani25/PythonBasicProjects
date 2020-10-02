from random import randint
number = randint(1,10)
name = input('Please enter your name:\n')
print('Hey',name+'! Welcome to the game- GUESS THE NUMBER!')
number_of_guess = 0

while number_of_guess < 5:
    guess = int(input())
    number_of_guess += 1
    if 1 <= guess <= 10 and 1 <= number <= 10:

        if guess < number:
            print('The number is lesser')
        elif guess > number:
            print('The number is greater')
        elif guess == number:
            print('The number you guessed is CORRECT. You WIN!!')
            break
        else:
            print('Sorry, you LOSE!! The correct number is',number)
    else:
        print('Check the number entered!')

if number_of_guess == 5:
    print('Thankyou.\n You dont have further guess left.')
else:
    print('Thankyou!')
