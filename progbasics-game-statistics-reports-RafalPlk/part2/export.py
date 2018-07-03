
# Export functions

from reports import *

def export_to_txt_2(file_name='game_stat.txt', exported_file_name2='exported_answers2.txt'):

    answers2 = ""
    answers2 += str(get_most_played(file_name)) + '\n'
    answers2 += str(sum_sold(file_name)) + '\n'
    answers2 += str(get_selling_avg(file_name)) + '\n'
    answers2 += str(count_longest_title(file_name)) + '\n'
    answers2 += str(get_date_avg(file_name)) + '\n'
    answers2 += str(get_game(file_name, '')) + '\n'

    with open (exported_file_name2, 'w+') as f:
        f.write(answers2)

export_to_txt_2()