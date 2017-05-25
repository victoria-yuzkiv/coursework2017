from modules.work_with_a_file import WorkWithAFile
from modules.series_research import SeriesResearch


class MainResearch:
    """

    """

    def __init__(self):
        """

        """
        file = WorkWithAFile("ratings.txt")
        file1 = file.open_file()
        my_lst = file.make_list(file1)
        self.series = SeriesResearch(len(my_lst))
        for i in range(self.series.find_len()):
            self.series.set_item(i, my_lst[i])

    def __str__(self):
        """

        :return:
        """
        series = ''
        for i in range(self.series.find_len()):
            series += self.series.get_item(i) + ' , '
        return series

    def popular_actors(self):
        """

        :return:
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

        :return:
        """
        seasons = {}
        for i in range(self.series.find_len()):
            try:
                seasons[self.series.get_item(i)] = self.series.seasons_number(i)
            except IndexError:
                continue
        return seasons

    def series_names(self):
        pass


def main():
    """

    :return:
    """

    series = MainResearch()
    a = series.popular_actors()
    for key, val in a.items():
        if val > 1:
            print(val, key)

    b = series.series_seasons()
    print(sorted(b.items(), key=lambda x: x[1]))

    # sorted(numbers.values())


main()
