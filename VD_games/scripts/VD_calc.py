"""Точка входа для игры 'Калькулятор'."""

from VD_games.engine import run_game
from VD_games.games import calc


def main() -> None:
    """Запуск игры."""
    run_game(calc, "VD Games - Calculator")


if __name__ == "__main__":
    main()
