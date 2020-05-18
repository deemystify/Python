#sometimes we copy and past our code. If you find yourself pasting the same version of your code in different areas of the program, 
#Maybe it's time to take a pause and use function. 

import datetime

# A function called print_time is created. 
def print_time():
        print('task completed')
        print(datetime.datetime.now())
        print()


first_name ='Lloyd'
print_time()

for x in range(0,10):
    print(x)
print_time()

# By moving the code to a functoin, you reduce reqork and the chance of introucing bugs., when you change the code you had copied

#import the datetime class from datetime library
# from datetime import datetime
# #Print the current time
# def print_time():
#     print('task completed')
#     #Now, we don't need the extra datetime prefix.
#     print(datetime.now())
#     print()

#What if I want a different message displayed?
# You can use function to accomplish this by passing paramaters

from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = 'Lloyd'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')
print()

# Here's another example where the code looks slightly different but we are doing the same logic 

first_name = input ('Enter your first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial + last_name_initial)

# Accomplishing the same task using a function

def get_initial(name):
    initial = name[0:1]
    return initial

first_name_initial = input('Enter your first name: ')
first_name_initial = get_initial(first_name_initial)

last_name = input('Enter your last name: ')
last_name = get_initial(last_name)

print('Your initials are: ' + first_name_initial + last_name_initial)

# Functions that return values allow clever code, but you might trade readability for less code

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your initials are: '\
    + get_initial(first_name_initial) \
        + get_initial(last_name_initial))

