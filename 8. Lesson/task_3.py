"""3. Написать декоратор для логирования типов позиционных аргументов функции
если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции"""

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num_list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({el}: {type(el)})' for el in num_list]
        print(*n, *func(*args, **kwargs), sep=',\n---')
    return wrapper


@type_logger
def calc_cube(*x, **y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in num_list]


a = calc_cube(5, 11, 8.9, ui=99.9, oi=6)
