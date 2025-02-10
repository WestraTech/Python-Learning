tpl = (2, 4, 6, 8) #Tuples are lists you DO NOT want to modify.

#As an example, "tpl[1] = 5" will only result in an error.
#It's also a good way to show collaberators that a list is supposed to be like that permanently.
#Printing elements works the same way it does with lists.

print(tpl.index(6)) #The number 6 is indexed as 2, so it will show this.

print(tpl + (10, 20)) #This works, but doesn't actually change the Tuple.


tpl = list(tpl)
tpl[0] = 5
tpl = tuple(tpl)
print(tpl) #THIS, however, does in fact work.