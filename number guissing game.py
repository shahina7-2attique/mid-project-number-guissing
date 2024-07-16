import random

guess_taken=0

print('welcome to number guessing game :)')
print("Hello! what's your name" )
player_name=input( )

number=random.randint( 1,100 )
print('well,' + player_name + ' i am thinking of number between 1 and 100' )

while guess_taken < 10:
    print('take a guess')
    guess=input( )
    guess=int(guess)

    guess_taken= guess_taken +1

    if guess < number :
        print('your guess is to low')  
    elif guess > number :
        print('your guess is too high')          
    else :
     guess_taken=str(guess_taken)
     print('good job, ' + player_name + ' you guess my number in,' + guess_taken + ' guess')
     break

if guess!=number:
    number =str(number)
    print('nope! the number i was thinking of was ' + number )

