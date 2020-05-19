#  Functions can accept multiple paramater


# def get_initial(name, force_upperCase):
#     if force_upperCase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial
# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name, False)

# print('Your initial is: ' + first_name_initial)

# You can specify a default value for a paramater

def get_initial(name, force_upperCase=True):
    if force_upperCase:
        initial = name[0:1].upper()
    else:
        initial=name[0:1]
        return initial
    first_name = input('Enter your first name: ')
    first_name_initial = get_initial(first_name)
    
    print('Your initial is: ' + first_name_initial)
    
    get_initial()
    
    # You can also assign the values to parameters by name when you call the function
    
    def get_initial(name, force_upperCase):
        if force_upperCase:
            initial = name[0:1].upper()
        else:
            initial = name[0:1]
            return initial
    first_name = input('Enter your first name: ')
    first_name_initial= get_initial(force_upperCase=True,  name=first_name_initial)
    
    print('Your initial is: ' + first_name_initial)
    
    # Using the named notation when calling functions makes your code more readable
    
    def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
        print('oh no error: ' + error_message)
        # Imagine code here that logs our error to a database or file
        
    first_number = 10
    second_number = 5
    if first_number > second_number:
        error_logger(error_code=45, error_severity=1, log_to_db=True, error_message='Second number greater than first', source_module='my_math_method') 
        