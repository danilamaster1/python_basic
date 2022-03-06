"""3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы"""

names_dict = {}


def thesaurus(*args):
    for i in args:
        if i[0] in names_dict.keys():
            names_dict[i[0]].extend([i])
        else:
            names_dict.setdefault(i[0], [i])
    return names_dict


print(thesaurus('Ad', 'Amma', 'Dan'))
