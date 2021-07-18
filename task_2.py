num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыри', 'five': 'пять', 'six': 'шесть',
            'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(word):
    if word.istitle():
        return str(num_dict.get(word.lower())).title()
    return num_dict.get(word)


print(num_translate(input('Введите число: ')))
