import os

my_list = {"my_project": [{"settings": []}, {"mainapp": []}, {"adminapp": []}, {"authapp": []}]}

for key, value in my_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
