"""6. Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки: для записи данных и
для вывода на экран записанных данных. При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
равный второму числу, включительно."""


from sys import argv

with open('bekery.csv', 'a', encoding='utf-8') as donut_a:
    with open('bekery.csv', 'r', encoding='utf-8') as donut_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace(',', '').isdigit()]:
            if len(argv) == 3:
                start, finish = map(int, argv[1:])
                print(*(v for i, v in enumerate(donut_r) if start - 1 <= i < finish), sep='')
            if ',' in argv[1] or '.' in argv[1]:
                print(f'{round(float(argv[1].replace(",", ".")), 3)}', file=donut_a)
            else:
                print(*(v for i, v in enumerate(donut_r) if i >= int(argv[1]) - 1))
        else:
            print(donut_r.read())
