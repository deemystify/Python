import helpers

helpers.display('Sample message', True)

from helpers import display
display('Sample MESSAGE')
# A simple sample module

def display(message, is_warning=False):
    if is_warning:
        print('This is a warning')
    print(message)
