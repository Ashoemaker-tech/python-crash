# A List is a collection which is ordered and cangable. Allows duplicates

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

#  Get a value
print(fruits[1])

#  Get Length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

#  Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

#  Remove with pop
fruits.pop(2)

#  Reverse the list
fruits.reverse()

#  Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

# iterate through list
for fruit in fruits:
    print(fruit)

text = 'Hello I like python'
# Slice operator slice(start:stop:step)
print(text[0:]) # if left empty then it will stop at the end fo str
print(numbers[1:])
numbers.slice[1:1]
