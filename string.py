# wow

if 1 > 0:
    print("1 is bigger than 0")
else:
    print("0 is bigger than 1")

contacts = {
    "Jimmy": 1,
    "Timmy": 10,
    "Finny": 100,
    "Minnie": 1000,
    "Cade": 10000,
    "Gabriel": 100000,
    "Bob": 1000000
}

client = input("Type smth:")

if client in contacts:
    print(client, contacts[client])
else:
    print(client, "Not found")

def fire(loaded):
    print("Loading ammo...")

    if loaded:
        print("Ready...")
        print("Aim..")
        print("FIRE!!!")
        print('''
              💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥
              💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥
              💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥
              ''')
    else:
        print("No ammo :(")

fire(False)