from matplotlib.pyplot import cla


class Control_Flow:

    class if_Statement:
        number = 23
        guess = int(input('Enter an integer : '))
        # Gets user input and puts it in the variable guess

        if guess == number:
            # New block starts here
            print('Congratulations, you guessed it.')
            print('(but you do not win any prizes!)')
            # New block ends here
        elif guess < number:
            # Another block
            print('No, it is a little higher than that')
            # You can do whatever you want in a block ...
        else:
            print('No, it is a little lower than that')
            # you must have guessed > number to reach here

        print('Done')
        # This last statement is always executed,
        # after the if statement is executed.

    class while_statement:
        number = 23
        running = True

        while running:
            # Will execute as long as running is True
            guess = int(input('Enter an integer : '))

            if guess == number:
                print('Congratulations, you guessed it.')
                # this causes the while loop to stop
                running = False
            elif guess < number:
                print('No, it is a little higher than that.')
            else:
                print('No, it is a little lower than that.')
        else:
            print('The while loop is over.')
            # Do anything else you want to do here

        print('Done')

    class for_Loop:
        for i in range(1, 5):
            print(i)
            # Does not print 5
        else:
            print('The for loop is over')

    class break_Statement:
        while True:
            s = input('Enter something : ')
            if s == 'quit':
                break
            print('Length of the string is', len(s))
        print('Done')

    class continue_Statement:
        while True:
            s2 = input('Enter something : ')
            if s2 == 'quit':
                break
            if len(s2) < 3:
                print('Too small')
                continue
            print('Input is of sufficient length')
