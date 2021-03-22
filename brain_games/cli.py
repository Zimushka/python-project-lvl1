"""Модуль приветствия."""
import prompt


def welcome_user():
    """Узнай имя, выведи его."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def main():
    """Выполни функцию."""
    welcome_user()


if __name__ == '__main__':
    main()
