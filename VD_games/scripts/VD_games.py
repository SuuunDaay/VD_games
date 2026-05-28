"""Основной модуль игры VD Games."""

from VD_games.cli import welcome_user


def main() -> None:
    """Главная функция модуля."""
    print("Welcome to VD Games!")
    welcome_user()


if __name__ == "__main__":
    main()
