import random
import test
from directory import category_dict
from directory import difficulty_dict
from directory import players_list

# соответственно изменился вывод категорий
for category_key, category_value in category_dict.items():
    print(f"{category_value}.{category_key}")
# изменилась логика проверки результатов и перехода


question_num = input("Введите номер желаемой категории: ")
while True:
    if int(question_num) in range(1, 11):
        break
    else:
        question_num = input("Введенное значение должно быть цифрой до 10 включительно, повторите ввод: ")
question_num_int = int(question_num)

players = input("Введите количество игроков(до 6): ")
while True:
    if int(players) in range(1, 7):
        break
    else:
        players = input("Введенное значение должно быть цифрой до 6 включительно, повторите ввод: ")
players_count = int(players)

i = 0
questions = test.resp()
players_list_new = random.sample(players_list, len(questions))
results_list = {}

for question in questions:
    i += 1
    print(f"внимание, вопрос № {i}")
    print(question.get('question'))
   # был исключен цикл определяющий сложность
    points = difficulty_dict[question.get('difficulty')]
    for player_in_game in players_list_new:
        player_answer = input(f"Игрок {player_in_game} введите ваш ответ: ")
        if player_answer.casefold() in question.get('correctAnswer').casefold():
            print(f"ваш ответ верный и вы заработали {points} очков")
            results_list[player_in_game] = points
            break
        else:
            print("к сожалению вы ответили неправильно")
            results_list[player_in_game] = 0
print("Игра окончена, результаты следующие:")
for player_name, player_points in results_list.items():
    print(player_name, player_points)
