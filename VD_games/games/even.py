import random


def print_rules() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_question() -> tuple:
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
