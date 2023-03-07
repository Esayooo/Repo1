#4
students = [
    ("Ерсанат", "Ерғалым"),
    ("Алия", "Оразбекова"),
    ("Аружан", "Баймолда"),
    ("Самғар", "Сабыржан"),
    ("Зарина", "Нурписова"),
    ("Ерасыл", "Байтанаев"),
]

for student in students:
    full_name = f"{student[0]} {student[1]}"
    if "ва" in full_name:
        print(full_name)
