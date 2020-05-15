#to get date and time in a neat and unique way for to present onscreen in a readable format
#use the timedelta library function. 
#refer to the below example. 

from datetime import timedelta # this fucntion calls the time delta library
from datetime import datetime 

today = datetime.now()
print ('Today is : ' + str(today))

yesterday = timedelta(days=1);

yesterday = today - yesterday
print('Yesterday was : ' + str( yesterday))

#dentions wil use timedelta to go back one week. 
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was : ' + str(last_week))

#use day, month, year, hour, minute, second functions 
#to display only part of the date. All these functions return intergers.
#Convert them to strings before concatenating them to another string. 

print ('Day: ' + str (today.day))
print ('Month: ' + str (today.month))
print ('Year: ' + str(today.year))
print ('Today, the ' + str(today.day) + 'th ' + ' of the ' + str(today.month)  + ' of the month marks the ' + str(today.day) + 'th  day in  the year' + str(today.year) + ', I am learning Python')

# Another example t odemonstrate the use of datetime delta

birth_day = input ('When is your birtday (dd/mm/yyy?')
birthday_date = datetime.strptime(birth_day, '%d/%m/%Y')
print('Birthday: ' + str(birth_day))