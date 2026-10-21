# Album object includes album attributes and stores collection of songs

from artist import Artist

class Album:
    def __init__(self, album_id, title, artist: Artist, release_date):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.release_date = release_date

        self.songs = []

        artist.add_album(self)

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def get_songs(self):
        return self.songs

    def get_artist(self):
        return self.artist

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_album_id(self):
        return self.album_id

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
