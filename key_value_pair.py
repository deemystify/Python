#You can create key": value JSON objects from a dictionary

# First, creat a dictinoary object 
import json

person_dict = {'First Name' : 'Lloyd', 'Last Name': 'Hart'}
#Add additional key pairs as needed to the dictionary
person_dict['City'] = 'Seattle'
# Create a list object of programming languages
language_list = ['CSharp', 'Python', 'JavaScript']
# Add list to dictionary
person_dict['languages']= language_list
# Second, convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_dict)

# Nest dictionaries to create JSON in the format {'Key':{subkey0':'subvalue0','subkey1':'subvalue1',..}
# Create staff dictionary which assigns a person to a role 

staff_dict = {}
staff_dict['Program Director'] = person_dict

# Convert dictionary to JSON object 
staff_json = json.dumps(staff_dict)

# Prints JSON object
print(staff_dict)