
# Printing functions

from reports import *


def print_get_most_played(file_name='game_stat.txt'):
    print('Most played game is {}.'.format(get_most_played(file_name)))


def print_sum_sold(file_name='game_stat.txt'):
    print('Total of sold copies are: {} millions'.format(sum_sold(file_name)))


def print_get_selling_avg(file_name='game_stat.txt'):
    print('Average selling is {:.0f} million copies.'.format(get_selling_avg(file_name)))


def print_count_longest_title(file_name='game_stat.txt'):
    print('The longest title has {} characters.'.format(count_longest_title(file_name)))


def print_get_date_avg(file_name='game_stat.txt'):
    print('Average number of years is {:.0f}'.format(get_date_avg(file_name)))


def print_get_game(file_name, title):
    properties = get_game(file_name, title)
    print('Properties of the game:\n')
    print('Title:', properties[0])
    print('Total copies sold:', properties[1])
    print('Release date:', properties[2])
    print('Genre:', properties[3])
    print('Publisher:', properties[4])



print_count_longest_title()
print_get_date_avg()
print_get_most_played()
print_get_selling_avg()
print_sum_sold()
print_get_game('game_stat.txt', "Half-Life")