#THere are only two major loops in python. 
#These are for and while. There is no other conditional loops. 

#Example of for loop in python. 

# for name in ['Lloyd', 'Susan', 'Bill', 'Gates', 'Jim', 'Skinny', 'Pinkett', 'Jasmine', 'Foster', 'Ethan', 'Jane', 'Jenny', 'Skyler', 'Dora', 'Simpson']:
#     print(name)

#How to loop x number of times? 
#Use a builtin loop function called range to automatically CREATE A list of number using the start and the number of itmes. 

# for index in range(0, 2):
#     print (index)

#Used on the previous example. 

names = ['Lloyd', 'Susan', 'Bill', 'Gates', 'Jim', 'Skinny', 'Pinkett', 'Jasmine', 'Foster', 'Ethan', 'Jane', 'Jenny', 'Skyler', 'Dora', 'Simpson']
index = 0
while index < len(names):
    print(names[index])
    #change the condition!!
    index = index + 1 #stack overflow occurs if the condition is not changed. 