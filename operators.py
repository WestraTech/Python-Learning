mood = ":(" #This assigns the value.

if mood != ":)": #!= means it cannot be equal to something.
    print("I am not happy.")

num = 1

if num > 0: #You can use <= to check for less than or equal to, and same with >= for greater than or equal to.
    print("bigger than 0")
elif num < 0:
    print("smaller than 0")
else:
    print("equal to 0")


total = int(input("Total: "))

print(type(total))

discount = 0

if total >= 100:
    discount = 10
elif total >= 50:
    discount = 5

print("Amount: ", total-discount)