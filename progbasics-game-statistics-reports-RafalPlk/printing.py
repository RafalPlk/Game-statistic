
# Printing functions

from reports import *

def print_count_games(file_name="game_stat.txt"):
    print("There are {0} games in {1} file.".format(count_games(file_name), file_name))


def print_decide(file_name, year):

    if decide(file_name, year):
        print('Yes, there\'s a game from year {}.'.format(year))
    else:
        print('No, there isn\'t any game from year {}.'.format(year))


def print_get_latest(file_name='game_stat.txt'):
    print("The latest game is {}.".format(get_latest(file_name)))


def print_count_by_genre(file_name, genre):
    print('There are {0} games in the {1} genre.'.format(count_by_genre(file_name, genre), genre))


def print_get_line_number_by_title(file_name, title):

    try:
        print('{0} is in {1} line.'.format(title, get_line_number_by_title(file_name, title)))
    except ValueError:
        print('There is no {0} game in {1}'.format(title, file_name))


def print_sort_abc(file_name='game_stat.txt'):

    for i in sort_abc(file_name):
        print(i)
