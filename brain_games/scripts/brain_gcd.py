# !/usr/bin/env python
# /home/zima/x_project/python-project-lvl1/.venv/bin/brain-gcd
"""Здесь будет доктайп."""

import math
from random import randrange

import prompt
from brain_games.scripts.brain_games import greet


def gcd_game():
    """Запусти игру НОД."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        f_number = randrange(1, 100)
        s_number = randrange(1, 100)
        core_answer = math.gcd(f_number, s_number)
        answer = prompt.string('Your answer: ')
        print('Question: {0} {1}'.format(f_number, s_number))
        if str(core_answer) == answer:
            if count < 3:
                count = count + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, core_answer))
            print("Let's try again, {0}!".format(name))
            break
        if count == 3:
            print('Congratulations, {0}!'.format(name))


def main():
    """Выполни main."""
    greet()
    gcd_game()


if __name__ == '__main__':
    main()
