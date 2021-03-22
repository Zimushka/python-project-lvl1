#!/usr/bin/env python3.9

"""test."""

from brain_games.cli import welcome_user


def greet():
    """Вызови функцию print."""
    print('Welcome to the Brain Games!')


def main():
    """Выполни main."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
