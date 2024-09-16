my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):
    current_el = my_list[index]
    if current_el >= 0:
        print(current_el)
        index += 1
    elif current_el < 0:
        index += 1
    else:
        break