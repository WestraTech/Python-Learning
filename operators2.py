total = int(input("Total: "))
discount = 0

if total < 100 and total >= 50: #This simply joins conditions using "and."
    discount = 10
elif total >= 100:
    discount = 5

print("Amount: ", total-discount)