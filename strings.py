# Strings can be either single or dbl quotes 

name = 'Andrew'
age = 31

# Concat
print('Hello my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-strings (3.6+)
print(f'Hello my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Cap string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list can take a delimiter as an arg to know what to split by
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# .strip() strips all white space from string 
print(s.strip())
