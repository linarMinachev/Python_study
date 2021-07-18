def thesaurus(*args):
    name_dict = {}
    for i in sorted(args):
        leter = i[0]
        if leter in name_dict:
            name_dict[leter] += [i]
        else:
            name_dict[leter] = [i]

    return name_dict


print(thesaurus('Линар', 'Андрей', 'Дмитрий', 'Максим', 'Сергей', 'Рустам', 'Айрат'))
