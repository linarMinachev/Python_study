from itertools import islice, zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

result = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(result))
print(*islice(result, 10))
print(*islice(result, 10))
