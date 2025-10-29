
'''
TASK A:
'''
x = 0 
while x < 4:
    num1 = user_guess_int
    randnum = randint(1,10)
    # user geanerates random number
    if num1 == randnum:
        print('you guessed right')
        print()
        print(f'Your answer was: {num1}')
        print()
        print(f'The number was: {randnum}')
        break
        # if the random number is equal to the users guess print the precieding messages
    else:
        print('Wrong number. ')
        print()
        print(f'The correct answer was: {randnum}')
        # if the random number is not equal to the user input the precieding messages
    x += 1
    if x == 4:
        print('Too many atempts')
# this code segment limmits the attemps a user has to 4 attempts
