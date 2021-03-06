
#------------------------------------------------------------

#CHAPTER 7 - Debugging

#------------------------------------------------------------

# Task 1: Using print to check data type

# The following code will give an error.
# Can you guess why? 

#userInput = input('please give a number ')
#result = userInput - 2
#print(result)

#Try checking the data type of input: 

userInput = input('please give a number ')
print(type(userInput))

#You can see that the input function automatically
#turns all input into a string. 
#Therefore we need to turn it into an int

# Task 2: Converting str into an int.

userInput = int(input('please give a number '))
result = userInput - 2
print(result)

#------------------------------------------------

# Script 2 page 73 - Nested function:

userInput = input('please give a number ')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return(result)

def nestedOperation():
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

# create a breakpoint by double clicking on the line
# number. 

result = simpleOperation(userInput)
result2 = nestedOperation()
print(result2)

#print(result2)

# Buttons: 

#  - first - runs your code until the break point.
#  - second - runs the code line-by-line, until the breakpoint.
#  - third - steps into the sections (class and functions). 
#  - fourth - steps out - for when you feel the error is not related to the current section.
#  - fifth - to go to the next breakpoint.
#  - last - square shaped button is to exit debugging mode and go back to normal coding mode.





