"""2. * (вместо 1) Найти IP адрес спамера и количество отправленных им
запросов по данным файла логов из предыдущего задания."""

import collections

with open('pars_logs.txt', 'r', encoding='utf-8') as f:
    my_d = collections.Counter()

    for i in f:
        i = i.split()[0]
        my_d[i] += 1

    ip, count = my_d.most_common(1)[0][0], my_d.most_common(1)[0][1]
    print(f'Spammer {ip} - {count} times')
