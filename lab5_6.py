list1 = [3, 5, 1, 9, 2, 7]
list2 = [1, 2, 3, 4, 5, 6]
def sorted_list(lst):
    if lst == sorted(lst):
        print(f"Тізім сұрыпталған")
        return True
    else:
        print(f"Тізім сұрыпталмаған")
        return False

print(sorted_list(list1)) 

print(sorted_list(list2)) 