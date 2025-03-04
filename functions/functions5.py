def log(*values, decor="-"):
    for val in values:
        val = str(val)
        len_val = len(val)

        prefix = (decor*2
            + decor*len_val
            + decor*2)

        print(prefix)
        print(decor + " " + str(val) + " " + decor)
        print(prefix)

print(10, end="\n") #\n means New Line
print(20)