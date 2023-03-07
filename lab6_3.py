#3
expenses = {
    "Түскі ас": 2000,
    "Жол шығын": 2100,
    "Кеңсе тауар": 500,
    "Басқа": 4000
}


Total = 0
for expense in expenses.values():
    Total += expense


print("Апталық жалпы шығындары: ", Total)
