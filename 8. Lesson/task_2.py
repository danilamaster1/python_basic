"""2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt"""

import re

check = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) .*$|^$')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        print(re.findall(check, line))
