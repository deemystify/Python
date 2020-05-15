#Error handling within a print statement. 
x = 42
y = 0

print() # used to create better visual for the program output
try:
   print(x / y)
   
   
except ZeroDivisionError as e:
    print('Not allowed to divide by zero'  )
else:
    print('Someting elsse went wrong ')
finally:
    print('This is our cleanup code')
print()