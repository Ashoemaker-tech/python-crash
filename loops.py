#  A loop is used for iterating over a sequence (that is either a list, a tuple, a dict, a set, or a string)

people = ['John', 'Andrew',  'Paul', 'Sarah']

# simple for loop
for person in people:
    print((f'Curent Person: {person}'))
    
# break
for person in people:
    if person == 'Sarah':
        break
    print(f'Current person: {person}')

# Continue
for person in people:
    if person == 'Sarah':
        continue
    print(f'Current person: {person}')
    
# range
for i in range(len(people)):
    print(people[i])
    
for i in range(0, 11): # 0 - 10
    print(f'Number: {i}')
# while loops execute a set of statements as long as a condition is true

count = 0
while count <= 10:
    print(f'Count:{count}')
    count += 1

