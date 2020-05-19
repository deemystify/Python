from datetime import datetime

# print timestaps to see how longs seciont of the code takes to run. 
# This is more like a unit testing. 


#using a function

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = 'Lloyd'
print_time('Task Completed')

for x in range (0,10):
    print (x)
print_time('Second completed for loop')

#Asking for someone's first, middle, and last names to print their inititals using function def.

def print_initials():
    first_name = input('Please enter your first name.')
    first_name_initial = first_name[0:1]

    middle_name = input ('Please enter your middle name: ')
    middle_name_initial = middle_name[0:1]

    last_name = input('Please enter your last name')
    last_name_initial = last_name[0:1]

    print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)
    print()

    # Anothe simpler implementation using the get option

    def get_initial(name):
        initial = name[0:1].upper
        return initial
    #Ask for someone's name and return the initials.
    first_name = input ('Enter your first name: ')
    first_name_initial = get_initial(first_name_initial)

    middle_name_initial = input ('Enter your middle name: ')
    middle_name_initial = get_initial(middle_name_initial)

    last_name_initial = input('Enter your last name: ')
    last_name_initial = get_initial(last_name_initial)

    print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)




print_initials()

