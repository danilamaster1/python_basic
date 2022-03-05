my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx, val in enumerate(my_list):
    if val.replace('+', '').replace('-', '').isdigit():
        if val.isdigit():
            my_list[idx] = f'"{int(val):02}"'
        else:
            my_list[idx] = f'"{val[0]}{int(val[1]):02}"'

print(" ".join(my_list))
