from pytvdbapi import api
db = api.TVDB("1D6897F57A08B0BA")


def actors():
    """
    Prints the information about actors, their roles and their photos (from "Sherlock").
    """
    result = db.search("Sherlock", "en")
    show = result[0]
    show.load_actors()
    for actor in range(len(show.actor_objects)):
        print(u"{0} - {1} - {2}".format(show.actor_objects[actor].Name, show.actor_objects[actor].Role,
                                        show.actor_objects[actor].image_url))


def seasons_and_episodes():
    """
    Prints the number of seasons in "Sherlock" and then prints the
    title of every episode.
    """
    result = db.search("Sherlock", "en")
    show = result[0]
    print("\n")
    print("The number of seasons: ", len(show))
    for episode in show[2]:
        print(episode.EpisodeName)


def show():
    """
    Prints the set of basic attributes and
    the full data set from the server.
    """
    result = db.search("dexter", "en")
    show = result[0]
    print(dir(show))  # List the set of basic attributes
    show.update()  # Load the full data set from the server
    print(dir(show))


def episode():
    """
    Prints information about 1 episode from 1 season in "Sherlock".
    """
    result = db.search("Sherlock", "en")
    show = result[0]
    episode = show[1][2]  # Get episode S01E02
    print(episode.season)
    print(episode.EpisodeNumber)
    print(episode.EpisodeName)
    print(episode.FirstAired)


def languages():
    """
    Prints the list of available languages.
    """
    for language in api.languages():
        print(language)


def search():
    """
    Searches episodes which have in their titles word
    "Sherlock". Prints it.
    """
    result = db.search("Sherlock", "en")
    print(result[0], "\n")
    for show in result:
        print(show)


def get_series():
    """
    Finds a series by its ID.
    """
    a = 79349
    show = db.get_series(a, "en")  # Load Dexter
    print("ID:", a, "\n", show.SeriesName)


def get_episode():
    """
    Finds episods by diven parameters.
    """
    ep = db.get_episode("en", episodeid=308834)  # id is the default method
    print(ep.EpisodeName, "\n")
    ep1 = db.get_episode("en", "dvd", seasonnumber=2, episodenumber=5, seriesid=79349)
    print(ep1.EpisodeName, "\n")
    ep2 = db.get_episode("en", "default", seasonnumber=2, episodenumber=6, seriesid=79349)
    print(ep2.EpisodeName, "\n")


def banner():
    """
    Prints the url link to banner of a certain series.
    """
    db = api.TVDB('B43FF87DE395DF56', banners=True)
    show = db.get_series(79349, "en")  # Dexter
    show.update()
    assert len(show.banner_objects) > 0
    banner = show.banner_objects[0]
    print(banner.banner_url)
    print(banner.Language)
