#Your code needs the ability to take different actions based on different conditions. 
#This is excatly what this file addresses using simple python conditional statements.

name = input ('Please type your first name here: ')
print()
print('Thank you,' + name + '!!')
price = input('Enter the   item price')
price = float(price)

try:
     if price >= 1.00:
         tax = .07
         print(float(tax))
         total = (tax/100) + float( price)
         print (str(total) + '$.00, is the total price for this item!')
        
except ZeroDivisionError as e:
     print('Wrong entry, please try again')
else:
    tax = 0
    print(str(tax) + '.00, paid for this item. Qualfies for free tax')
finally:
     print('Thank you for using our item pricing application!! Good Bye!!')



    #Careful when comparing strings.
country = input('Enter your country: ')


if country.lower()  == 'canada':
        print('Oh look a Canadian!')
else:
        print('You are not from Canada')
    
