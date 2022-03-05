tr_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}


def num_translate(word):
    if word.istitle():
        return str(tr_dict.get(word.lower())).title()
    return tr_dict.get(word)


print(num_translate('Four'))
print(num_translate('two'))
