"""
With matching, you take get your code from this:

mood = input("How are ya feelin' today, bud?")
if mood == ":)":
    print("Yippee!")
elif mood == ":(":
    print("WaHhhHHhHh!!")
elif mood == ":/":
    print("Meh..")
elif mood == ":D":
    print("YAYYYYYYYYY")
elif mood == ":O":
    print("Wowzers!")
elif mood == ":3":
    print("Meow")
else:
    print("Hello world!") 

to this:
"""

match input("How are ya feelin' today, bud?"):
    case ":)":
        print("Yippee!")
    case ":(":
        print("WaHhhHHhHh!!")
    case ":/":
        print("Meh..")
    case ":D":
        print("YAYYYYYYYYY")
    case ":O":
        print("Wowzers!")
    case ":3":
        print("Meow")

    case mood:
        print(mood, "Hello World!")

# (This only works with Python 3.10)