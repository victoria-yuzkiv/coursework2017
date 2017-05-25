from modules.my_research import *

series = MainResearch()


def test_actors():
    """
    >>> test_actors()
    [('Jesse Plemons', 3), ('Martin Freeman', 3)]
    """
    actors_list = []
    allactors = series.popular_actors()
    for key, val in allactors.items():
        if val > 1:
            actors_list.append((key, val))
    a = sorted(actors_list, key=lambda x: x[1], reverse=True)[0:2]
    return sorted(a, key=lambda x: x[0])


def test_seasons():
    """
    >>> test_seasons()
    [('The Simpsons', 29), ('Doctor Who', 27), ('ER', 16)]
    """
    allseasons = series.series_seasons()
    return sorted(allseasons.items(), key=lambda x: x[1], reverse=True)[0:3]


def test_titles():
    """
    >>> test_titles()
    [('The', 16), ('And', 3)]
    """
    alltitles = series.series_titles()
    return sorted(alltitles.items(), key=lambda x: x[1], reverse=True)[0:2]


test_actors()
test_seasons()
test_titles()
