my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(my_list):
    if v.replace("+", "").replace("-", "").isdigit():
        if v.isdigit():
            my_list[i] = f"'{int(v):02}'"
        else:
            my_list[i] = f"'{v[0]}{int(v[1:]):02}'"

print(" ".join(my_list))
