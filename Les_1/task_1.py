duration = int(input("Введите кол-во секунд: "))

res_time = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]
print(f'Дней: {res_time[0]:02} {res_time[1]:02}:{res_time[2]:02}:{res_time[3]:02}')