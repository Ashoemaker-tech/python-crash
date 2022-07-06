# A function is a block of code which only runs whin it is called. In python we do nto use curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name = 'Sam'):
    print(f'Hello {name}')
    
# Return Values
def getSum(num1, num2):
    total = num1 + num2
    return total


# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but van only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))

