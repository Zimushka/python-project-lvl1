# !/usr/bin/env python
# /home/zima/x_project/python-project-lvl1/.venv/bin/brain-calc
"""Здесь будет доктайп."""

from random import choice, randrange

import prompt
from brain_games.scripts.brain_games import greet


def calc_game():
    """Запусти игру калькулятор."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        operators = ['+', '-', '*']
        f_number = randrange(1, 50)
        s_number = randrange(1, 50)
        oper_random = choice(operators)
        print('Question: {0} {1} {2}'.format(f_number, oper_random, s_number))
        correct_answer = eval((str(f_number) + str(oper_random) + str(s_number)))
        answer = prompt.string('Your answer: ')

        if str(correct_answer) == answer:
            if count < 3:
                count = count + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            break
        if count == 3:
            print('Congratulations, {0}!'.format(name))


def main():
    """Выполни main."""
    greet()
    calc_game()


if __name__ == '__main__':
    main()
