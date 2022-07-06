# python has functions for creating reading updating and deleting files.

#  open a file
myFile = open('myfile.txt', 'w')

# get info on file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# write to file
myFile.write('I love python')
myFile.write(' and Javascript')
myFile.close()

# append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I started with PHP')
myFile.close()

# read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)



