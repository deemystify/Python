#YOu may need to check multiple conditions to determine the correct action 

#province = 'Alberta', 'Nunavut', 'Ontario'
#province = input('Enter your province: ')

# if province == 'Alberta':
#     tax = 0.05
#     print(tax)

# elif  province == 'Nunavut': #when you use elif instead of multiple if statments, you can add a default action 
#     tax = 0.05
#     print(tax)

# elif province == 'Ontario':
#     tax = 0.013
#     print(tax)

# else:
#     tax = 0.15
#     print (str(tax) + '% tax rate for every other provinces within Canada. ')

    #If multiple conditions cause the same action, they can be combined into a single condition 

# if province == 'Alberta' or province == 'Nunavut':
#         tax = 0.05
# elif province == 'Ontario':
#         tax = 0.13
# else:
#         tax = 0.15

# The IN operator is used to check a list of possible values. 
#Refer to the following example.

# if province in ('Alberta', 'Nunavut', 'Yukon')
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15

# If an action depends on a combination of conditions you can nest if statements. 
country = input('Enter your country: ')
if country  == 'Canada' : 
    if province in('Alberta', 'Nunavut', 'Yukon'):
         tax = 0.05
    elif province == 'Ontario':
            tax = 0.13
    else:
            tax = 0.15
else:
            tax = 0.0



