from requests import get, utils
from re import findall

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def cur_rates(code):
    v, s = findall(rf'({code.upper()}).+?(\d+\,\d+)', response)[0]
    return f'{v} {s.replace(",", ".")}'


print(cur_rates("USD"))
print(cur_rates("EuR"))