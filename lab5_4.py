values=[]
while True:
    n=(int(input('n:')))
    values += [n]
    if n==0:
        break
print(sorted(values,reverse=True))
