# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

my_list = [n ** 3 for n in range(1000)][1::2]
print('Задание 2)', my_list)

# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

sum_of_numbers = 0

for idx, val in enumerate(my_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_of_numbers += my_list[idx]

print('Задание 2_а)', sum_of_numbers)
# 17485588610 - контрольная сумма


# b and c) К каждому элементу списка добавить 17
# Вычислить сумму чисел из этого списка, сумма цифр которых делится нацело на 7.

sum_of_numbers = 0

for i in range(len(my_list)):
    my_list[i] = my_list[i] + 17

for ind, value in enumerate(my_list):
    sum_digits = 0
    while value > 0:
        sum_digits += value % 10
        value //= 10
    if sum_digits % 7 == 0:
        sum_of_numbers += my_list[ind]

print('Задание 2_b_c)', sum_of_numbers)
# 15392909930 - контрольная сумма
