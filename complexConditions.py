#Sometimes you can combine conditions with AND instead of nesting if statements. 

#Example based a sample applcation

##################################################
# Requirements for honour roll 
# Minimum 85% grade point average 
# Lowest grade is atleast 70%
# A student makes honour roll if their average is greater than 85%
####################################################

# gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('You made the honour roll')
# else:
#     print('You did not make the honour roll. You will need to work harder!')


#If you need to remember the results of a condition check later in your code, use 
#Boolean variables as flags

#1. Check to see if the requirmens for honour roll are met

gpa = float(input('What was your Grade Point Average? '))
lowest_grade= float (input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made honour roll!')
