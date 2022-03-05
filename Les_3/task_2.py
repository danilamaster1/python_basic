names_dict = {}


def thesaurus(*args):
    for i in args:
        if i[0] in names_dict.keys():
            names_dict[i[0]].extend([i])
        else:
            names_dict.setdefault(i[0], [i])
    return names_dict


print(thesaurus('Ad', 'Amma', 'Dan'))
