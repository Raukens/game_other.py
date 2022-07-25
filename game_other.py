import random
import requests

from reference import category_dict
from reference import difficulty_dict
from reference import players_list

# соответственно изменился вывод категорий
for category_key, category_value in category_dict.items():
    print(f"{category_value}.{category_key}")
# изменилась логика проверки результатов и перехода


category_numb = input("Введите номер желаемой категории: ")
while True:
    if int(category_numb) in range(1, 11):
        break
    else:
        category_numb = input("Введенное значение должно быть цифрой до 10 включительно, повторите ввод: ")
category_numb = int(category_numb)

players = input("Введите количество игроков(до 6): ")
while True:
    if int(players) in range(1, 7):
        break
    else:
        players = input("Введенное значение должно быть цифрой до 6 включительно, повторите ввод: ")
players = int(players)

question_category = category_dict[int(category_numb)]
questions_url = "https://the-trivia-api.com/api/questions?categories=" + str(question_category) + "&limit=" + str(
    players)
questions = requests.get(questions_url).json()


i = 0

players_list = random.sample(players_list, len(questions))
results_dict = dict.fromkeys(players_list, 0)
for question in questions:

    points = difficulty_dict[question.get('difficulty')]
    print(f"внимание игрок {players_list[i]}, ваш вопрос № {i+1} со сложностью {points}:")
    print(question.get('question'))
    player_answer = input(f"Введите ваш ответ: ")
    player_answer = player_answer.casefold()
    correct_answer = question.get('correctAnswer').casefold()
    print(players_list)
    if player_answer in correct_answer:
        print(f"Поздравляем, ваш ответ верный. Вы заработали {points} очков")
        results_dict[players_list[i]] += points
        i += 1
    else:
        print("к сожалению вы ответили неправильно")
        new_players = list(players_list)
        new_players.remove(players_list[i])
        print(new_players)
        for player in new_players:
            player_answer = input(f"Игрок {player} введите ваш ответ: ")
            player_answer = player_answer.casefold()
            if player_answer in correct_answer:
                print(f"Поздравляем, ваш ответ верный. Вы заработали {points} очков")
                results_dict[player] += points
                break
            else:
                print("к сожалению вы ответили неправильно")
        i += 1
print("Игра окончена, результаты следующие:")
for player_name, player_points in results_dict.items():
    print(player_name, player_points)