
# Export functions

from reports import *

def export_to_txt(file_name='game_stat.txt', exported_file_name='exported_answers.txt'):

    answers = ""
    answers += str(count_games(file_name)) + '\n'
    answers += str(decide(file_name, 2000)) + '\n'
    answers += str(get_latest(file_name)) + '\n'
    answers += str(count_by_genre(file_name,'')) + '\n'
    answers += str(get_line_number_by_title(file_name, 'Guild Wars')) + '\n'
    answers += str(sort_abc(file_name)) + '\n'

    with open(exported_file_name, 'w+') as f:
        f.write(answers)

export_to_txt()
