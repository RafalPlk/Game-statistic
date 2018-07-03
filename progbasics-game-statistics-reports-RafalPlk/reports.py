
# Report functions


def count_games(file_name):

    with open(file_name, 'r') as f:
        counter = 0
        for line in f:
            counter += 1
        return counter


def decide(file_name, year):

    with open(file_name, 'r') as f:
        for line in f:
            lists_of_lines = line.split("\t")
            if str(year) == lists_of_lines[2]:
                return True
            else:
                continue
        return False


def get_latest(file_name):
    
    with open(file_name, 'r') as f:
        latest = 0
        title = 0
        for line in f:
            lists_of_lines = line.split("\t")
            if int(lists_of_lines[2]) > int(latest):
                latest = lists_of_lines[2]
                title = lists_of_lines[0]
    return title


def count_by_genre(file_name, genre):

    with open(file_name, 'r') as f:
        counter = 0
        for line in f:
            lists_of_lines = line.split("\t")
            if genre == lists_of_lines[3]:
                counter += 1
        return counter


def get_line_number_by_title(file_name, title):

    with open(file_name, 'r') as f:
        counter = 0
        titles = []

        for line in f:
            counter += 1
            lists_of_lines = line.split("\t")
            if lists_of_lines[0] == title:
                return counter
            if title != lists_of_lines[0]:
                titles.append(lists_of_lines[0])

        for i in titles:
            if title not in titles:
                raise ValueError


def sort_abc(file_name):

    with open(file_name, 'r') as f:
        unsorted_titles = []
        sorted_titles = []

        for line in f:
            lists_of_lines = line.split("\t")
            unsorted_titles.append(lists_of_lines[0])
        while unsorted_titles:
            smallest = min(unsorted_titles)
            sorted_titles.append(smallest)
            unsorted_titles.pop(unsorted_titles.index(smallest))
        return sorted_titles
