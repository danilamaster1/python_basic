"""5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
из трех случайных слов, взятых из трёх списков (по одному из каждого)

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?"""

from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj)

    while count and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_j.append(f"{no.pop(num)} {adv.pop(num)}, {adj.pop(num)}")
        else:
            list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        count -= 1
    return list_of_j


print(get_jokes(3))



