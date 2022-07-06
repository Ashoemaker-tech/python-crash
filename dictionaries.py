# A Dictionary is a collection which is unordered, changable and indexed. No duplicate members

#  Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Get value
print(person['first_name'])
print(person.get('last_name')) # get method

# Add key/value
person['phone'] = '555-555-5555'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove an item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])