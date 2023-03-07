
def get_grades():
    grades = {
        'Anna':{"Math": 90, "English": 85, "physics": 95},
        'Mary': {"Math": 95, "English": 95, "physics": 100},
        'Peter': {"Math": 85, "English": 95, "physics": 80}
    }
    student_name = input('Please enter name: ')

    if student_name in grades:
        return grades[student_name]
    else:
        print('Error.')
        return []


print(get_grades())






