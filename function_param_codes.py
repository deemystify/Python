############################################
#   This function will take a name and return the 
#   First letter of the name

def get_initial(name, force_upperCase=True):
    if force_upperCase:
        
        initial = name[0:1].upper()
    else: 
        initial = name[0:1]
    return initial

# Ask for someone's name and return the initials
first_Name = input('Enter your first name: ')
first_Name_Initial= get_initial(force_upperCase=False, name=first_Name) # Named notation is used here. 

print( ' Your initial is: ' + first_Name_Initial) 

