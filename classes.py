# A class is like a blueprint for creating objects. An object has properties and methods associated with it. Almost everything in python is an object.

# create a class
import email


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
            
    def has_birthday(self):
        self.age += 1
            
            
#  extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance
            
            
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
# init user obj
Andrew = User('Andrew Shoemaker', 'test@test.com', 31)

#  init customer
janet = Customer('Janet Johnson', 'janet@test.com', 25)

janet.set_balance(500)

print(janet.greeting())

Andrew.has_birthday()
print(Andrew.greeting())

