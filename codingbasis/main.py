import random                   # importing python random library

guess = 0                       # initializing the number of guesses variable

rand = random.randint(1, 100)           # assingning the umber generared by random to variable(rand)

while True:                     # starting a while loop so my program will keep working

    enter = input('Guess the random number: ')          # display msg to user to input a number and assing number to variable

    if enter == 'stop':             # check if the number is stop word
        break

    number = int(enter)             # converting string into number

    if 1<= number <=100 :           # cheking if number is betwenn 1 and 100

        if number == rand:          # checking if the user guess was right
            print('Congratulations you guess the right number ', number)
            guess +=1
            print('You guss was right for  ', guess, ' times')
            break

        elif number > rand:         # if the user entered higher number
            print('Oh sorry ', number, ' is higher. Try again.')
            continue

        elif number < rand:         # if the user entered lower number
            print('Oh sorry ', number,' is lower, Try again.')

    else:                           # if the user enter number less than 1 or more than 100
        print('Please enter a number between 1 and 100')

