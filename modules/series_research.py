from pytvdbapi import api
from modules.an_array import AnArray

db = api.TVDB("1D6897F57A08B0BA")


class SeriesResearch:
    """
    Implements the SeriesResearch ADT for doing
    research based of the information about series.
    """

    def __init__(self, length):
        """
        Creates an array.

        :param length: the length of a created array.
        """
        self.allseries = AnArray(length)

    def get_item(self, index):
        """
        Gets the value of the element.

        :param index: the index of the element.
        :return: value of the element.
        """
        return self.allseries.__getitem__(index)

    def set_item(self, index, value):
        """
        Puts the value in the array element at index position.

        :param index: the index the element.
        :param value: the value of the element.
        """
        self.allseries.__setitem__(index, value)

    def get_actors(self, index):
        """
        Gets actors from series (the value of the element is
        the name of series).

        :param index: the index of the element.
        :return: the list of actors.
        """
        series = self.get_item(index)
        actors = []
        result = db.search(str(series), "en")
        show = result[0]
        show.load_actors()
        for actor in range(len(show.actor_objects)):
            actors.append(show.actor_objects[actor].Name)
        return actors

    def seasons_number(self, index):
        """
        Gets the number of seasons in the given series
        (the value of the element is the name of series).

        :param index: the index of the element.
        :return: the number of seasons.
        """
        series = self.get_item(index)
        result = db.search(str(series), "en")
        show = result[0]
        return len(show)
