#Tax computation using the if and other condiational statements.
#Simple approach. 

# province = input ('What province do you live in? ')
# tax = 0;

# if province == 'Alberta':
#     tax = 0.05
# if province == 'Nunavut':
#     tax = 0.05
# if province == 'Ontario':
#     tax = 0.13
# print(tax)

#Another implementation using elif. makes the program more dynamic.

# if province == 'Albertha':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.15
# print(tax)

#A third varition of the same program using the In statment to reduce the amount of code. 

country = input('What country do you live in? ')

if country != 'Canada':
    tax = 0.00
    print(str('You qualify for ' + str(tax) + 'in taxes, because you live outside of Canada. Thank you for your business!'))
elif  country == 'Canada':
    province = input ('What province do you live in? ')

if province in ('Alberta', 'Nunavut') :
     tax = 0.05
     print(tax)
elif province == 'Ontario':
     tax = 0.13
     print(tax)

else: #Every other province not lised in Alberta, means the customer lives in another country and will there 
    tax = 0.15
    
print (str('You do not live within our discounted province, therefore, your tax is, ' + str(tax) + '%'))