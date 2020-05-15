#The following lines of code will ask the user for a name, date of birth, and provide responses based on the user input
 
from datetime import datetime, timedelta

print ('\n----------------------------------------\nFileName:     yourName.py\nDescription:     This is a demo Application Written in Python \n                 That accepts the user input and provides output\nWritten by:      Lloyd Harris\nDate:            5/14/2020\n---------------------------------------- ')

today = datetime.now()

name = input ('Please type your name here: ')
print ('Thank you, ' + name)
print ('Are you interested in knowing your horoscope?')
age = input('Enter your age here to for answers you did not know existed: ')
print (str (age) + ' is your current age')
