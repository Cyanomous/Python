
class Basics:

    print("Hello World")
    # This is a comment

    class Numbers:
        num1 = 2  # This is a whole number
        num2 = 3.32  # This is a float or floating point number

    class Strings_And_Quotes:
        string1 = "Hello World"  # This is a string
        # The '' thingies are the single quotes
        string2 = 'I am encased in single quotes'
        string3 = "I am encased in double quotes"  # The "" thingies are double quotes
        string4 = """"I am encased in triple quotes"""  # The """""" thingies are triple quotes
        # You can also uses single quotes and double quotes freely in triple quotes
        # Triple quotes can also be multi-line
        string5 = """
        I am a triple quote
        I can have multiple lines
        You can also use 'single quotes' and "double quotes" freely within me
        """

    class Format_Methods:
        age = 20
        name = "Joe Smith"

        print("{0} was {1} years old when he wrote this book".format(name, age))
        # You could also do:
        print(name + " was " + str(age) + " years old when he wrote this book")
        # or
        print(f"{name} was {age} years old when he wrote this book")
        # This is called an f string because there is an f before the quotes

        print("a", end=' ')  # This adds a space to the end
        print("b", end=' ')  # This also adds a space to the end
        print("c")

        print("This is the first line\nThis is the second line")
        # This creates a new line after the \n

        print(r"\n wont make a newline because this is a raw string")
        # Adding a r before the string makes the string a raw string
        # Raw strings just print everything as it is

    class Examples:
        i = 5
        print(i)
        i = i + 1
        print(i)

        s = """This is a multi-line string.
        THis is the second line."""
        print(s)

    class Logical_And_Physical_Line:
        s2 = "This is a string. \
            This continues the string"
        # Using \ allows you to contine what you are doing on another line
        # So you could do: print\
        #                       (s2)
        # and it would be the same as print(s2)
        print(s2)
