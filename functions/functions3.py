def log(val, decor):
    val = str(val)
    len_val = len(val)

    prefix = decor*2 + decor*len_val + decor*2

    print(prefix)
    print(decor + " " + str(val) + " " + decor)
    print(prefix)

log(3, "*")
log(68, "-")
log(102, "#")
log(1000000, ".")
log(decor="O", val=100) #Keyword Argument