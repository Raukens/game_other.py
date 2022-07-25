from reference import difficulty_dict


def check_cats(category_numb, cats_count):
    while True:
        if int(category_numb) in range(1, cats_count+1):
            break
        else:
            category_numb = input("Введенное значение должно быть цифрой до 10 включительно, повторите ввод: ")
    category_numb = int(category_numb)
    return category_numb


def check_players(players, max_players):
    while True:
        if int(players) in range(1, max_players + 1):
            break
        else:
            players = input("Введенное значение должно быть цифрой до 6 включительно, повторите ввод: ")
    players_count = int(players)
    return players_count


def check_conditions(questions, players_list):
    i = 0
    results_dict = dict.fromkeys(players_list, 0)
    for question in questions:

        points = difficulty_dict[question.get('difficulty')]
        print(f"внимание игрок {players_list[i]}, ваш вопрос № {i+1} со сложностью {points}:")
        print(question.get('question'))
        player_answer = input(f"Введите ваш ответ: ")
        player_answer = player_answer.casefold()
        correct_answer = question.get('correctAnswer').casefold()
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