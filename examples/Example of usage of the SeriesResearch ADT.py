from modules.series_research import SeriesResearch


def example():
    """
    The example of usage of the SeriesResearch ADT.
    """
    # Creates a new array (length = 2)
    new_array = SeriesResearch(2)

    # Sets values to each element of the array.
    new_array.set_item(0, "Sherlock")
    new_array.set_item(1, "Doctor Who")

    # Gets values and prints it.
    print("Item 0 = ", new_array.get_item(0))
    print("Item 1 = ", new_array.get_item(1))

    # Gets lists of actors.
    actors0 = new_array.get_actors(0)
    actors1 = new_array.get_actors(1)

    # Prints these lists.
    print(actors0)
    print(actors1)

    # Finds the number of seasons in series.
    seasons0 = new_array.seasons_number(0)
    seasons1 = new_array.seasons_number(1)

    # Prints the number of seasons.
    print("The number of seasons in", new_array.get_item(0), ":", seasons0)
    print("The number of seasons in", new_array.get_item(1), ":", seasons1)

example()
