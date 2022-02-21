
class Functions:

    class Functions:
        def say_hello():
            # Makes the function and its name
            print('hello world')

        say_hello()  # Calls the function
        say_hello()  # Functions can be called multiple times

    class Function_Perameters:
        def print_max(a, b):
            if a > b:
                print(a, 'is maximum')
                # If a is greater than b it will print "a is maximum"
            elif a == b:
                print(a, 'is equal to', b)
                # If a is the same number as b it will print "a is equal to b"
            else:
                print(b, 'is maximum')
                # If b is greater than a it will print "b is maximum"

        # directly pass literal values
        print_max(3, 4)

        x = 5
        y = 7

        # pass variables as arguments
        print_max(x, y)

    class Local_Variables:
        x = 50

        def func(x):
            print('x is', x)
            x = 2
            print('Changed local x to', x)

        func(x)
        print('x is still', x)

    class Global_Variables:
        x = 50

        def func():
            global x

            print('x is', x)
            x = 2
            print('Changed global x to', x)

        func()
        print('Value of x is', x)

    class Default_Values:
        def say(message, times=1):
            # By adding a =1 after times, the value of times is automatically set to 1
            print(message * times)

        say('Hello')
        say('World', 5)
        # We can overide the default value of 1, by adding a new value

    class Keyword_Arguments:
        def func(a, b=5, c=10):
            print('a is', a, 'and b is', b, 'and c is', c)

        func(3, 7)
        func(25, c=24)
        func(c=50, a=100)

    class VarArgs_Parameters:
        def total(a=5, *numbers, **phonebook):
            print('a', a)

            # iterate through all the items in tuple
            for single_item in numbers:
                print('single_item', single_item)

            # iterate through all the items in dictionary
            for first_part, second_part in phonebook.items():
                print(first_part, second_part)

        total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)

    class Return:
        def maximum(x, y):
            if x > y:
                return x
            elif x == y:
                return 'The numbers are equal'
            else:
                return y

        print(maximum(2, 3))

    class DocStrings:
        def print_max(x, y):
            '''Prints the maximum of two numbers.

            The two values must be integers.'''
            # convert to integers, if possible
            x = int(x)
            y = int(y)

            if x > y:
                print(x, 'is maximum')
            else:
                print(y, 'is maximum')

        print_max(3, 5)
        print(print_max.__doc__)
