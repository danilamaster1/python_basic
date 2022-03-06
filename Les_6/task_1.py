"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
 web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
 — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). """

with open('pars_logs.txt', 'w', encoding='utf-8') as p:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        content = (f'{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}' for line in f)
        for i in content:
            print(i, file=p)