#Self is always the first parameter in a init method, and refers to the 
# instance of the class that we're creating, or the current job ---
# the other parameter are the value for the propreties that we want to initialize

class Robot_dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    #Method
    def bark(self):
        print('Wooof')
        
# Main program
my_dog= Robot_dog('Indio', 'Pitbull')
print(my_dog.name)
print(my_dog.breed)
#method
my_dog.bark()