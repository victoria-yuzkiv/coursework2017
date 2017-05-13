from modules.work_with_a_file import WorkWithAFile
from modules.series_research import SeriesResearch


# in progress (it's 4th stage)

class MainResearch:

    def __init__(self):

        file = WorkWithAFile("ratings.txt")
        file1 = file.open_file()
        my_lst = file.make_list(file1)
        self.series = SeriesResearch(len(my_lst))
        for i in range(self.series.find_len()):
            self.series.set_item(i, my_lst[i])

    def __str__(self):
        for i in range(self.series.find_len()):
            print(self.series.get_item(i))

    def popular_actors(self):
        pass

    def series_seasons(self):
        pass

    def series_names(self):
        pass


def main():

    series = MainResearch()
    print(series)


main()
