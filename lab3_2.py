A = int(input("A="))
B = int(input("B="))
if A<B:
    for number in range (A,B+1):
        print(number)
else:
    for number in range(A,B-1,-1):
        print(number)
