import requests

from directory import category_dict

from game import question_num_int
from game import players_count


# question_num_int = 4
# players_count = 3
def resp():
    for key, value in category_dict.items():
        if question_num_int == value:
            question_category = key
    questions_url = "https://the-trivia-api.com/api/questions?categories=" + str(question_category) + "&limit=" + str(
        players_count)
    response_list = requests.get(questions_url).json()
    return response_list
