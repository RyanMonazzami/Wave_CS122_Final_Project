# library stores all songs, albums, and artists and also handles searching and filtering


class Library:
    def __init__(self):
        self.songs = []
        self.albums = []
        self.artists = []

    def add_song(self, song):
        if song in self.songs:
            return False
        self.songs.append(song)
        self.add_artist(song.artist)
        if song.album is not None:
            self.add_album(song.album)
        return True

    def add_album(self, album):
        if album in self.albums:
            return False
        self.albums.append(album)
        self.add_artist(album.artist)
        return True

    def add_artist(self, artist):
        if artist in self.artists:
            return False
        self.artists.append(artist)
        return True

    def search_songs(self, query):
        query = query.strip().lower()
        return [song for song in self.songs if query in song.title.lower()]

    def search_albums(self, query):
        query = query.strip().lower()
        return [album for album in self.albums if query in album.title.lower()]

    def search_artists(self, query):
        query = query.strip().lower()
        return [artist for artist in self.artists if query in artist.name.lower()]

    def search(self, query):
        return {
            "songs": self.search_songs(query),
            "albums": self.search_albums(query),
            "artists": self.search_artists(query),
        }

    def filter_by_genre(self, genre):
        genre = genre.strip().lower()
        return [song for song in self.songs if song.genre.lower() == genre]

    def filter_by_artist(self, artist_name):
        artist_name = artist_name.strip().lower()
        return [song for song in self.songs if song.artist.name.lower() == artist_name]

    def filter_by_album(self, album_title):
        album_title = album_title.strip().lower()
        return [song for song in self.songs
                if song.album is not None and song.album.title.lower() == album_title]

    def filter_songs(self, title=None, artist=None, album=None, genre=None):
        results = self.songs
        if title:
            title = title.strip().lower()
            results = [song for song in results if title in song.title.lower()]
        if artist:
            artist = artist.strip().lower()
            results = [song for song in results if song.artist.name.lower() == artist]
        if album:
            album = album.strip().lower()
            results = [song for song in results
                       if song.album is not None and song.album.title.lower() == album]
        if genre:
            genre = genre.strip().lower()
            results = [song for song in results if song.genre.lower() == genre]
        return list(results)

    def get_genres(self):
        return sorted({song.genre for song in self.songs})

    def sort_songs(self, songs=None, key="title", reverse=False):
        if songs is None:
            songs = self.songs
        sort_keys = {
            "title": lambda song: song.title.lower(),
            "artist": lambda song: song.artist.name.lower(),
            "album": lambda song: song.album.title.lower() if song.album else "",
            "genre": lambda song: song.genre.lower(),
        }
        if key not in sort_keys:
            raise ValueError(f"Cannot sort by '{key}'")
        return sorted(songs, key=sort_keys[key], reverse=reverse)
