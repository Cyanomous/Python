
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
