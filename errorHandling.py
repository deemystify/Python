#Syntax Errors. Found in the source code of a program as a reulst of a missing semicolon, bracket, etc. 
#the codeset below won't run at all due to syntax error. 

# x = 42
# y = 206
# if x == y
#      print ('Success!!')

#Runtime errors. Occurs during the runtime of the application. provide more information on where to start debugging. 
#Example: The below codeset will fail when run

# x = 42
# y = 0
# print (x / y) 

#cATCHING RUNTIME ERRORS

try: 
    print(x / y)
except ZeroDivisionError as e:
    #Optionally, log e somewhere
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')

#Logic Errors. See below example. This code won't run at all. 
#By definition, a logic error is an error that will allow a code to compile with no syntax errors, or noticeable issue. No runtime error. But it just doesn't give
#the response we are looking for. 

x = 206
y = 42
if x < y:
    print(str(x) + ' is greater than ' + str(y))
