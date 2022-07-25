import random

import check

import test

from reference import category_dict
from reference import players_list


# соответственно изменился вывод категорий
for category_key, category_value in category_dict.items():
    print(f"{category_key}.{category_value}")
cats_count = 10
max_players = 6

category_numb = input("Введите номер желаемой категории: ")
check.check_cats(category_numb, cats_count)
players = input("Введите количество игроков(до 6): ")
check.check_players(players, max_players)

questions = test.resp(category_numb, players)
players_list = random.sample(players_list, len(questions))

check.check_conditions(questions, players_list)