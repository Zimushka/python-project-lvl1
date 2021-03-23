#!/usr/bin/env python3.9

"""Здесь будет доктайп."""

# Начало импорта
import prompt
from random import randint
# Конец импорта

print('Answer "yes" if the number is even, otherwise answer "no"')

i = 0
while i < 3:
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    answer = prompt.string('Your answer: ')

    if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 != 0 and answer == 'no'):
        i = i + 1
        print('Correct!')
    else:
        i = 0
        print('Incorrect!')  # Вставить правильный вывод инкорректа + добавить имя


