"""Игра: Калькулятор (сложение, вычитание, умножение)."""

import random


def print_rules() -> None:
    """Выводит правила игры."""
    print("What is the result of the expression?")


def generate_question() -> tuple:
    """
    Генерирует случайное математическое выражение.

    Returns:
        tuple: (question_text, correct_answer)
    """
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(["+", "-", "*"])

    question = f"{num1} {operation} {num2}"

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:  # operation == '*'
        correct_answer = num1 * num2

    return question, correct_answer
