class Resume: 
    
    def __init__(self, name, age): #Init is a method called automatically by Python.
        self.name = name
        self.age = age

Jake = Resume("Jake", 21)
Jake.age = 20 #Can modify attributes.

print(Jake.age)

del(Jake.age) #Deletes the attribute.

#print(Jake.age)
#This will cause an error in Python.