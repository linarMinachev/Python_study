def odd_nums_31(number):
    for number in range(1, number + 1, 2):
        yield number


for i in odd_nums_31(31):
    print(i)
