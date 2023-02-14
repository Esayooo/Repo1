a=input("Enter numer1:")
b=input("Enter number2:")
while not(a.isdigit() and b.isdigit()):
    a=input("Enter numer1:")
    b=input("Enter number2:")
print(int(a)+int(b))

