# Argument

def get_user_name():
    name = input("What's your name? ")
    if name != "":
        print ("Hello " + name.capitalize())
    else:
        print ("Hello World")

get_user_name()

