"""3. Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка."""


class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    try:
        num = input('введите число (f для выхода): ')
        if num.isdigit():
            num = int(num)
        elif num == 'f':
            print(f'конец - {my_list}')
            break
        else:
            raise MyErr('нужно число!')
    except MyErr as err:
        print(err)
    else:
        my_list.append(num)
        print(my_list)
