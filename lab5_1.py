students = []
while True:
    name = input("Please enter student's name: ")
    if not name:
        break
    group = int(input("Enter group: "))
    students.append((name, group))

students.sort(key=lambda student: student[1])

for student in students:
    print(f"{student[0]} - {student[1]} группа")

