my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
format_list = []

for i in my_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            format_list.append(f"'{int(i):02}'")
        else:
            format_list.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        format_list.append(i)

print(" ".join(format_list))
