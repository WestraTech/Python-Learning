counter = 0

while counter != 4:
    print("start")
    counter += 1

    if(counter % 2) != 0:
        continue

    print(counter)
    print("end")