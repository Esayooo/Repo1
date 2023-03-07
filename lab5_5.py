import random

numbers = []
while len(numbers) < 6:
    num = random.randint(1, 49)
    if num not in numbers:
        numbers.append(num)

numbers.sort()
print("Сіздің билетіңіз: ", numbers)