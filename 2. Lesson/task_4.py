"""4. Дан список, содержащий искажённые данные с должностями и именами сотрудников
Известно, что имя сотрудника всегда в конце строки.
Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка,
как привести их к корректному виду. Можно ли при этом не создавать новый список?
"""

worker = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in worker:
    print(f'Привет, {i.split()[-1].capitalize()}!')
