def log(*values, decor="-"): #Value was made into a tuple. Now using multiple values is much easier to do.
    for val in values:
        val = str(val)
        len_val = len(val)

        prefix = (decor*2
            + decor*len_val
            + decor*2)

        print(prefix)
        print(decor + " " + str(val) + " " + decor)
        print(prefix)

log(2, 4, 8, 16, 32, 64, 128)