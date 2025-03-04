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

try:
    print(client, contacts[client])
except KeyError:
    print(client, "not found!")