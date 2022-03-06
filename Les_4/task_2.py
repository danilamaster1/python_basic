"""2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.

3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.

5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
"""

from sys import argv
from datetime import date
from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    content = response.split('Valute ID=')
    d, m, y = map(int, content[0].split('"')[-4].split('.'))
    for i in content:
        if code.upper() in i:
            print(date(year=y, month=m, day=d), end=', ')
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    word = argv[1]
    print(currency_rates(word))
