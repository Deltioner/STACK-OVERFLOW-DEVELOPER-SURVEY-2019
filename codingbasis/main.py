import random

guess = 0

rand = random.randint(1, 100)

while True:

    enter = input('Guess the random number: ')

    if enter == 'stop':
        break
    number = int(enter)

    if 1<= number <=100 :

        if number == rand:
            print('Congratulations you guess the right number ', number)
            guess +=1
            print('You guss was right for  ', guess, ' times')

            continue

        elif number > rand:
            print('Oh sorry ', number, ' is higher. Try again.')
            continue

        elif number < rand:
            print('Oh sorry ', number,' is lower, Try again.')

    else:
        print('Please enter a number between 1 and 100')

