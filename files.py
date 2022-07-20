# python has functions for creating reading updating and deleting files.

# #  open a file
# myFile = open('myfile.txt', 'w') # write mode clears the file and writes what is input to the file

# # get info on file
# print('Name: ', myFile.name)
# print('Is Closed: ', myFile.closed)
# print('Opening Mode: ', myFile.mode)

# # write to file
# myFile.write('I love python') # use the escape '\n' to write to next line
# myFile.write(' and Javascript')
# myFile.close()

# # append to file
# myFile = open('myfile.txt', 'a')
# myFile.write(' I started with PHP')
# myFile.close()

# # read from file
# myFile = open('myfile.txt', 'r+')
# text = myFile.read(100)
# print(text)

from asyncore import read


file = open('myfile.txt', 'r') # opens file in read mode
f = file.readlines() # prints escape chars at end of each line

newlist = []
# check for escape and remove escape from each line in file
# for line in f:
#     if line[-1] == '\n':
#         newlist.append(line[:-1])
#     else:
#         newlist.append(line)   

# one liner
for line in f:
    newlist.append(line.strip()) 
print(newlist)



