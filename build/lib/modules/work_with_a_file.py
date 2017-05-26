# Class WorkWithAFile is created to read information from a file
# ratings.txt and to convert it into a list of series names.


class WorkWithAFile:
    """
    Contains functions open_file() and make_list().
    To work with this class you should specify a filename.
    """

    def __init__(self, filename):
        """
        Creates an empty list.
        :param filename: the name of a file.
        """
        self.series = []
        self.filename = filename

    def open_file(self):
        """
        Opens a file and saves all the information in a list
        (split by newlines).
        :return: a list with all the information from the file.
        """
        all_series = []
        openfile = open(self.filename, encoding="utf-8")
        whole_file = openfile.readline()
        while not whole_file.endswith("Forgotten Lady (Season 5, Episode 1)"):
            whole_file = openfile.readline()
            all_series.append(whole_file)
        return all_series

    def make_list(self, lst):
        """
        Creates a list of series names.
        :param lst: a list with all the information from the file.
        :return: a list of series names.
        """
        for i in range(0, len(lst), 5):
            if i < 45:
                self.series.append(lst[i][3:-1])
            else:
                self.series.append(lst[i][4:-1])
        for name in range(len(self.series)):
            if "(" in self.series[name]:
                self.series[name] = self.series[name][:self.series[name].index("(") - 1]
        return self.series
