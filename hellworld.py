# first_name = 'Lloyd'
# print (first_name)
# last_name = 'Harris'
# print (first_name + last_name)
# print ('Hello ' + first_name + ' ' + last_name)
# sentence = 'The dog is named Sammy'
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.count('a'))

#The functions help us format strings we save to files and databases, or display to users
#first_name = input('what is your first name?')
#last_name = input('what is your last name?')
#print ('Hello ' + first_name.capitalize() + ' ' \
    #+ last_name.capitalize())


    #Custom String Formatting

# first_name = input ('What is your first name?')
# last_name = input ('What is your last_name?')
# output = 'Hello, ' + first_name + ' ' + last_name
# print (output)
# output = 'Hello, {} {}'.format(first_name, last_name)
# print (output)
# output = 'Hello, {0} {1}' .format(first_name, last_name)
# print (output)
# #only available in python 3
# output = f' Hello, {first_name} {last_name}' 
# print (output)

#Toggling between various outputs

first_name = 'Lloyd '
last_name  = 'Harris'

#output = 'Hello, ' + first_name + ' ' + last_name

#output = 'Hello,  {} {}' .format(first_name, last_name)
#output = 'Hello,  {0} {1}' .format(first_name, last_name)
#output = f' Hello, {first_name} {last_name} '
#print (output) 

# # You cna do math with numbers in python
# first_num = 6
# second_num = 2
# print (first_num + second_num)
# print(first_num ** second_num) #double asterix represents expontents in python 
# print (first_num * second_num)

# # Python gets confused when you combine strings with numeric datatypes. The below  will result in error.  
# days_in_May = 31
# #print(days_in_May + ' days in May')
# #type convresion.using string.
# # When displaying a string that contains numbers you must convert the numbers into strings.

# print (str(days_in_May) + ' days in May') 

# num_1 = '5'
# num_2 = '6'

# print (num_1 + num_2)

# first_num = input('Enter first number')
# second_num = input ('Enter second number')
# print (first_num + second_num)
# # Example converting entry to int before outputing the result. 

# print (int(first_num) + int (second_num))
# print (float (first_num) + float (second_num))

# #Testing out numberins python
#  pi = 3.145159
#  print (pi)



# first_num =  input ('Please enter a number: ')
# second_num = input ('Please enter another number: ')

# print (int(first_num) +  int (second_num))
# print  (int (first_num) * int (second_num))
# print (int (first_num) ** int (second_num))
# days_in_February = 28
# print (str(days_in_February) + 'total days in February' )

#Working with dates in python. tO GET CURRENT DATE AND TIME, we need to use the datetime library 
#From datetime import dataetime. 

# from datetime import datetime

# current_date = datetime.now()
# #the neow function returns a datetime object
# print ('Today is : ' + str (current_date))

# #timedelta is used to define a period of time
# from datetime import timedelta
# today = datetime.now()
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print ('Yesterday was: ' + str( yesterday))

#Use date functions to control date formatting 

# print ('Day: ' + str (current_date.day))
# print ('Month: ' + str (current_date.month))
# print ('Year: ' + str (current_date.year))
#print ('My current date is ' + str(current_date.day) + ' ' +  str(current_date.month))

#sometimes you receive the date as a string and need to convert it to a datetime object

# birthday = input('When is your birthday (dd/mm/yyyy)? ' )

# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

# print ('Birthday: ' + str(birthday_date))

# #What was the day before my birthday

# day_before_my_birtday = timedelta(days =1)
# birthday_eve= birthday_date  - day_before_my_birtday

# print ('Day before my birtday was: ' + str(birthday_eve))

# To get current date and time, we need to use the dattime library
from datetime import datetime
from datetime import timedelta 

current_date = datetime.now() #Now functoin returns curren date and time as a datetime object

#You must convert the datetime object to a sring before you can concatenate to another string. 

print ('Today is: ' + str(current_date))