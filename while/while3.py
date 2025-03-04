def fire(rounds):
    print("Loading Ammo")
    print("FIRE!!!")

    while True:
        if rounds:
            print("BLAM")
            rounds -= 1
        else:
            print("reload")
            break #Breaks out of a loop.

fire(6) #Fires 6 times.