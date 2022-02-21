class Data_Structures:

    class List:
        # This is my shopping list
        shoplist = ['apple', 'mango', 'carrot', 'banana']

        print('I have', len(shoplist), 'items to purchase.')
        # len() returns the length of an object

        print('These items are:', end=' ')
        for item in shoplist:
            print(item, end=' ')
            # Prints the items in the shopping list with a space in between each object

        print('\nI also have to buy rice.')
        shoplist.append('rice')
        # Adds the item rice to the bottom of the list
        print('My shopping list is now', shoplist)

        print('I will sort my list now')
        shoplist.sort()
        # Sorts the list
        print('Sorted shopping list is', shoplist)

        print('The first item I will buy is', shoplist[0])
        olditem = shoplist[0]
        # shoplist[0] is the first item in the list
        del shoplist[0]
        # Deletes the first item in the list
        print('I bought the', olditem)
        print('My shopping list is now', shoplist)

    class Tuple:
        # I would recommend always using parentheses
        # to indicate start and end of tuple
        # even though parentheses are optional.
        # Explicit is better than implicit.
        zoo = ('python', 'elephant', 'penguin')
        print('Number of animals in the zoo is', len(zoo))

        new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
        print('Number of cages in the new zoo is', len(new_zoo))
        print('All animals in new zoo are', new_zoo)
        print('Animals brought from old zoo are', new_zoo[2])
        print('Last animal brought from old zoo is', new_zoo[2][2])
        # new_zoo[2][2] acceses the third item of the third line
        print('Number of animals in the new zoo is',
              len(new_zoo)-1+len(new_zoo[2]))

    class Dictionary:
        # 'ab' is short for 'a'ddress'b'ook

        ab = {
            'Swaroop': 'swaroop@swaroopch.com',
            'Larry': 'larry@wall.org',
            'Matsumoto': 'matz@ruby-lang.org',
            'Spammer': 'spammer@hotmail.com'
        }
        # The strings before the ":" are called keys, keys need to be strings

        print("Swaroop's address is", ab['Swaroop'])
        # ab['Swaroop'] acceses the item for the key 'Swaroop'

        # Deleting a key-value pair
        del ab['Spammer']

        print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

        for name, address in ab.items():
            print('Contact {} at {}'.format(name, address))

        # Adding a key-value pair
        ab['Guido'] = 'guido@python.org'

        if 'Guido' in ab:
            print("\nGuido's address is", ab['Guido'])

    class Sequence:
        shoplist = ['apple', 'mango', 'carrot', 'banana']
        name = 'swaroop'

        # Indexing or 'Subscription' operation #
        print('Item 0 is', shoplist[0])
        print('Item 1 is', shoplist[1])
        print('Item 2 is', shoplist[2])
        print('Item 3 is', shoplist[3])
        print('Item -1 is', shoplist[-1])
        # Note: adding the "-" before the number means you start from the back
        print('Item -2 is', shoplist[-2])
        print('Character 0 is', name[0])

        # Slicing on a list #
        print('Item 1 to 3 is', shoplist[1:3])
        # Note: shoplist[1:3] will only return the second item and third item not the fourth
        print('Item 2 to end is', shoplist[2:])
        print('Item 1 to -1 is', shoplist[1:-1])
        print('Item start to end is', shoplist[:])

        # Slicing on a string #
        print('characters 1 to 3 is', name[1:3])
        print('characters 2 to end is', name[2:])
        print('characters 1 to -1 is', name[1:-1])
        print('characters start to end is', name[:])

    class References:
        print('Simple Assignment')
        shoplist = ['apple', 'mango', 'carrot', 'banana']
        # mylist is just another name pointing to the same object!
        mylist = shoplist

        # I purchased the first item, so I remove it from the list
        del shoplist[0]

        print('shoplist is', shoplist)
        print('mylist is', mylist)
        # Notice that both shoplist and mylist both print
        # the same list without the 'apple' confirming that
        # they point to the same object

        print('Copy by making a full slice')
        # Make a copy by doing a full slice
        mylist = shoplist[:]
        # Remove first item
        del mylist[0]

        print('shoplist is', shoplist)
        print('mylist is', mylist)
        # Notice that now the two lists are different

        # Basically, mylist = shoplist does not make a copy of shoplist and name it mylist.
        # Instead it just refers back to shoplist
        # So in order to make a copy you need to do, mylist = shoplist[:]

    class More_Strings:
        # This is a string object
        name = 'Swaroop'

        if name.startswith('Swa'):
            print('Yes, the string starts with "Swa"')

        if 'a' in name:
            # Checks if the letter a is the the string a
            print('Yes, it contains the string "a"')

        if name.find('war') != -1:
            print('Yes, it contains the string "war"')

        delimiter = '_*_'
        mylist = ['Brazil', 'Russia', 'India', 'China']
        print(delimiter.join(mylist))
        # Joins the items in mylist with _*_(Prints the items with _*_ between them)
