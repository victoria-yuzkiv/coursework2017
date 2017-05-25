from modules.work_with_a_file import WorkWithAFile
from modules.series_research import SeriesResearch


class MainResearch:
    """
    This class represents methods which help to do some research.
    """

    def __init__(self):
        """
        Reads the information from a file.
        Makes an array which contains that information.
        """
        file = WorkWithAFile("ratings.txt")
        file1 = file.open_file()
        my_lst = file.make_list(file1)
        self.series = SeriesResearch(len(my_lst))
        for i in range(self.series.find_len()):
            self.series.set_item(i, my_lst[i])

    def __str__(self):
        """
        Creates a string with series titles.

        :return: a string with series titles
        """
        series = ''
        for i in range(self.series.find_len()):
            series += self.series.get_item(i) + ' , '
        return series

    def popular_actors(self):
        """
        Creates a dictionary. Gets the information about all
        actors from given series and adds it to the dictionary
        (key - the name of an actor/actress, value - the number of series
        in which that actor/actress performed).

        :return: a dictionary (key - the name of an actor/actress, value -
        the number of series in which that actor/actress performed)
        """
        actors = {}
        for i in range(self.series.find_len()):
            try:
                actors_from_series = self.series.get_actors(i)
                for actor in actors_from_series:
                    if actor not in actors:
                        actors[actor] = 1
                    else:
                        actors[actor] += 1
            except IndexError:
                continue
        return actors

    def series_seasons(self):
        """
        Creates a dictionary. Gets the information about number of seasons
        in series adds it to the dictionary (key - series title, value - the number
        of seasons).

        :return: a dictionary (key - series title, value - the number of seasons).
        """
        seasons = {}
        for i in range(self.series.find_len()):
            try:
                seasons[self.series.get_item(i)] = self.series.seasons_number(i)
            except IndexError:
                continue
        return seasons

    def series_titles(self):
        """
        Creates a dictionary. Gets every word from series titles and adds it
        to the dictionary(key - word, value - the number of repetition in
        series titles).

        :return: the dictionary(key - word, value - the number of
        repetition in series titles).
        """
        words = {}
        for i in range(self.series.find_len()):
            word = self.series.get_item(i).split()
            for k in word:
                if k not in words:
                    words[k] = 1
                else:
                    words[k] += 1
        return words


def save_info(info, filename):
    """
    Creates a new file with a name filename.
    Writes the information from info into this file.

    :param info: a list of tuples with the information
    that should be saved.
    :param filename: a name of a created file.
    """
    thefile = open(filename, 'w')
    for item in info:
        thefile.write(str(item[1]) + " - " + str(item[0]) + '\n')


def main():
    """
    Makes the main research.
    """
    series = MainResearch()

    # actors
    actors_list = []
    allactors = series.popular_actors()
    for key, val in allactors.items():
        if val > 1:
            actors_list.append((key, val))
    save_info(sorted(actors_list, key=lambda x: x[1], reverse=True), "popular_actors.txt")

    # seasons
    allseasons = series.series_seasons()
    save_info(sorted(allseasons.items(), key=lambda x: x[1], reverse=True), "series_seasons.txt")

    # titles
    alltitles = series.series_titles()
    save_info(sorted(alltitles.items(), key=lambda x: x[1], reverse=True), "series_titles.txt")


main()
