# If/Esle conditions are used to decide to do something based on something being true or false

x = 3
y = 5


#  Comparison operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')
    
#  if else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')


# elif

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if
if x > 2:
    if x < 10:
        print(f'{x} is less than 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than 10')
#  or 
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than 10')
# not
if not(x > 2 and x <= 10):
    print('not reverses the outcome of the paranthesis')

# Membership operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

# In
if x in numbers:
    print(x in numbers)
    
#  not in
if x not in numbers:
    print(x not in numbers)
    
# Identity operators (is, is not ) - compare the objects
a = 2
b = 2

# is
if a is b:
    print(a is b)

# is not
if a is not b:
    print(a is not b)

