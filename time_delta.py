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