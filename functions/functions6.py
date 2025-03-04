def log(*values, decor="-", end="\n", padding=2):
    for val in values:
        val = str(val)
        len_val = len(val)

        prefix = (decor*padding
                + decor*len_val
                + decor*padding)
        
        output = (decor * (padding - 1)
                  + " " + str(val) + " "
                  + decor * (padding - 1))

        print(prefix)
        print(output)
        print(prefix, end=end)

log(10, 20, decor="~", padding=4)

#Simplifies everything by creating more variables.