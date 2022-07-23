import requests

from directory import category_dict


def resp(question_num_int, players_count):
    question_category = category_dict[question_num_int]
    questions_url = "https://the-trivia-api.com/api/questions?categories=" + str(question_category) + "&limit=" + str(
        players_count)
    response_list = requests.get(questions_url).json()
    return response_list
