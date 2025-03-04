def log(val):
    val = str(val)
    len_val = len(val)

    prefix = "--" + "-"*len_val + "--"

    print(prefix)
    print("- " + str(val) + " -")
    print(prefix)

log(3)
log(68)
log(102)
log(1000000)