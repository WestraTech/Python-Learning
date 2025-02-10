list1 = [ 1, 1, 2.0, 3, ]
list2 = ["Blue", "Purple", "Indigo", "Red"]

print( list2[0]) #Prints the first one.
print( list2[1:]) #Prints the 2nd through the rest.

list3 = ["Watermelon", "Pear", "Plum" ]

list3[2] = "Mulberry" #This changes Plum to Mulberry.

print(list3)

list2.remove("Purple") #Deletes Purple from the List2 list.

print(list2)

list3.pop(2) #Removes the 3rd item from the list.

print(list3)

list3.append("Apple-Pear Hybrid") #Adds Apple-Pear Hybrid to the 3rd list.

print(list3)

list3 = list3 + ["Blueberry"] #Adds Blueberry to the 3rd list.

print(list3)

list3.extend(["Blackberry", "Golden Raspberry"]) #Adds Blackberry and Golden Raspberry to List3.

print(list3)

print( len(list2) ) #Shows how many items are in List2.

print( sum(list1) ) #Prints the sum of all numbers in list1.
print( max(list1) ) #Prints the highest value in list1.
print( min(list1) ) #Prints the lowest value in list1.

list1.append(1.6)

list1.sort() #Sorts list1 from lowest to greatest.

print(list1)

list1.sort(reverse=True) #Sorts list1 from greatest to lowest.

print(list1)