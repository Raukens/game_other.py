import requests

from reference import category_dict


def resp(category_numb, players):
    question_category = category_dict[int(category_numb)]
    questions_url = "https://the-trivia-api.com/api/questions?categories=" + str(question_category) + "&limit=" + str(
        players)
    response_list = requests.get(questions_url).json()
    return response_list
