num = 10.017

if num.is_integer():
    num = int(num) #Decimal places will not be affected if the decimals are 0.

print(num)

num = int(num) if num.is_integer() else num #If/else statements work like this.
print(num)