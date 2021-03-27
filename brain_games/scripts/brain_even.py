#!/usr/bin/env python3.9
# /home/zima/x_project/python-project-lvl1/.venv/bin/brain-even
"""Здесь будет доктайп."""

from random import randrange

import prompt
from brain_games.scripts.brain_games import greet


def even_game():
    """Запусти игру проверка на четность."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count = 0
    while count < 3:
        random_number = randrange(1, 100)
        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer: ')

        if random_number % 2 == 0 and answer == 'yes':
            count = count + 1
        elif random_number % 2 != 0 and answer == 'no':
            count = count + 1

        else:
            if answer == 'yes':  # Господи, костыль на костыле
                re_answer = 'no'      # Это ужасно, но это НАКАНЕЦТА РАБОТАЕТ
            else:                # В рот мне ноги, на это ушло четыре дня, Карл!
                re_answer = 'yes'

            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, re_answer))
            print("Let's try again, {0}!".format(name))
            break
        if count == 3:
            print('Congratulations, {0}!'.format(name))


def main():
    """Выполни main."""
    greet()
    even_game()


if __name__ == '__main__':
    main()
