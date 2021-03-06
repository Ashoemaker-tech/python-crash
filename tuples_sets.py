# A Tuple is a collection which is ordered and unchangable. Allows duplicate members

# Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Delete tuple
del fruits2

# define length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if something is in a set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')


# remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)



