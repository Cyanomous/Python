class Modules:

    class Example:
        import sys

        print('The command line arguments are:')
        for i in sys.argv:
            print(i)

        print('\n\nThe PYTHONPATH is', sys.path, '\n')

    class Module_Using_Name:
        if __name__ == '__main__':
            print('This program is being run by itself')
        else:
            print('I am being imported from another module')

    class My_Module:
        def say_hi():
            print('Hi, this is mymodule speaking.')

        __version__ = '0.1'  # You can view the version using file name.__version__ if its imported
