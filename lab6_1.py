#1
s1=()
s2=()

def fill_tuple(a,b):
    return tuple(range(a,b))

s1=fill_tuple(0,6)
s2=fill_tuple(-5,1)
s3=s1+s2
count_zero = s3.count(0)
print(f"s3: {s3}")
print(f"Count of zeros: {count_zero}")
