values = []
while True:
    value = int(input("Бүтін сан енгізіңіз:"))
    try:
        values.append(value)
        if value == 0:
            break
    except ValueError:
        print("Қате!")

sorted_values = sorted(values)

for value in sorted_values:
    print(value)
