#Lists are collectoin sof items. More fluid and can use differenty kinds of datatypes in contrast to arrays  
#Below are examples of common operations that can be performed on a list. 

names = ['Lloyd', 'Anne'] # prepoluated list
print(len(names)) # Get the number of items 
names.insert(0, 'Bill'); # Insert before index. 
names.sort()
print(names)
scores = []# empty list
scores.append(89) # Add new item to the end of  the list. 
scores.append(99)
print(str(names) + ' are all the names on our list')
print('The scores are: ')
print(scores)
print(str(scores[1]) + ' is the first score on our list') # Collections are zero-index

###############################################################################################
#  Arrays are also collections of items To use arrays in python, 
#   You will need to make an axplicit call from the collections library 
#   See below example. 
#   Arrays can be numberic data type and can only store the same kind of data types. 
#################################################################################################

from array import array

scores = array('d')# d is an indcation of a double numberic data type that will be used in the array 
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])# PRINTS THE 2nd ITEM in the array 


 
