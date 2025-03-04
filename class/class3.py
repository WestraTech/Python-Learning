class Resume: 
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(my):
        len_name = len(my.name)

        print(" -" + "-"*len_name + "- ")
        print("| " + my.name + " |")
        print(" -" + "-"*len_name + "- ")

Jake = Resume("Jake", 21)

Jake.show()