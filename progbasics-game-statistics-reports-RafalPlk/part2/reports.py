
# Report functions


def get_most_played(file_name):

    title = ""
    copies = 0

    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")
            if float(lists_of_lines[1]) > float(copies):
                copies = lists_of_lines[1]
                title = lists_of_lines[0]
    return title

def sum_sold(file_name):
    total = float(0)

    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")
            total += float(lists_of_lines[1])
    return total


def get_selling_avg(file_name):

    games_number = 0
    total = float(0)

    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")
            total += float(lists_of_lines[1])
            games_number += 1
        avg = total / games_number
    return avg


def count_longest_title(file_name):

    title_char_length = 0
    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")
            if len(lists_of_lines[0]) > title_char_length:
                title_char_length = len(lists_of_lines[0])
    return title_char_length


def get_date_avg(file_name):

    year_count = 0
    years_sum = 0
    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")
            years_sum += int(lists_of_lines[2])
            year_count += 1
        avg = years_sum / year_count
    return round(avg)


def get_game(file_name, title):

    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")

            if lists_of_lines[0].lower() == title.lower():
                lists_of_lines[1] = float(lists_of_lines[1])
                lists_of_lines[2] = int(lists_of_lines[2])

                if '\n' in lists_of_lines[4]:
                    lists_of_lines[4] = lists_of_lines[4][:-1]
                return lists_of_lines
