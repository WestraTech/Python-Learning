set = {1, 2, 3, 4, 4} #Creating a set. Curly brackets are what you use to make one.
print(set)

print("""The set has the values 1, 2, 3, 4, and 4.
Duplicates will not be stored, therefore, only one 4 will be shown.""")

set.add(5) #Use this code to add something to a set.
print(set)

set.remove(1) #Use this code to remove something from a set.
print(set)

set.discard(6)
print(set) #If 6 is in the set, it will be removed. If not, there will be no error. Use this as sort of an if/else statement. Using st.remove() on a value that does not exist will cause an error.

foods = {"Taco", "Pizza", "Beans", "Cake", "Apple", "Rice", "Chocolate", "Red Velvet", "Watermelon", "Banana"}
desserts = {"Cake", "Chocolate", "Red Velvet", "Cupcakes", "Brownies"}

print(desserts.intersection(foods)) #This will print every item these sets have in common.
print(desserts.difference(foods)) #This will print every item from the desserts set that is not in the food set.
print(desserts.symmetric_difference(foods)) #This will print every item these sets do not have in common.