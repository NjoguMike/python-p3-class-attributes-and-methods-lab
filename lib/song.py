# from collections import Counter

class Song:

    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        
    
    @classmethod
    def add_song_to_count(
        cls,value = 1):
        cls.count += value
        
    @classmethod
    def add_to_genres(cls,genre):
        if genre in cls.genres:
            Song.add_to_genre_count(genre)
        else:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            Song.add_to_artist_count(artist)
        else:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.genre_count[genre] += 1
        pass
    
    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] += 1
        pass

# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("99 Problems", "Jay Z", "Rap")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# print(Song.genre_count)
# print(Song.artists)
# print(Song.genres)
# print(Song.add_to_genre_count())