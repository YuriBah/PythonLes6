from json import dump
from itertools import zip_longest

with open('users.csv.txt', 'r', encoding='utf-8') as users:
    with open('hobby.csv.txt', 'r', encoding='utf-8') as hobby:

        if len(users.readlines()) > len(hobby.readlines()):
            with open('dict_n_h.json', 'w', encoding='utf-8') as f:
                all_list = zip_longest(users, hobby, fillvalue=None)
                my_dict = {str(el[0]).strip(): (el[1].strip()) for el in all_list}

                dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)