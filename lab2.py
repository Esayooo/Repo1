name= input("What is your name?")
phone =input("Enter your phone number:")
print(name+phone)
a = input("a:")
b = input("b:")
def bigger(a,b):
    if a>b:
        print("%s is bigger" %a)
    elif a<b:
        print("%s is bigger" %b)
    else:
        print("%s is equal to %s" %(a,b))
    return 'The end'

bigger(a,b)


