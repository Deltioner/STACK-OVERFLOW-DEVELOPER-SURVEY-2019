import random        # importing random library

rand = random.randint(1, 100)  # assigning the generated number by random into the variable(rand)

while True:             # while true loop so the program will continue working

        enter = input('Guess the random number: ')      # assigned the input inserted by user into the variable(enter)

        if enter == "stop":             # if loop to check if the user enter the word(stop)
            break
        number = int(enter)             # converting the input from string to integer

        if 1 <= number <= 100:          # checking if the input is between 1 and 100
            if number == rand:
                print('You guess the number ', number)
                break

            elif number > rand:          # if the number entered is higher than the random number generated
                print('Sorry this number is higher ', number)
                continue

            elif number < rand:          # if the number guessed is lower than the random number generated
                print("Sorry this number is lower", number)

        else:                            # if the number entered by the user was less than 1 or more than 100
            print("You are out of range please choose between 1 and 100")
            break

