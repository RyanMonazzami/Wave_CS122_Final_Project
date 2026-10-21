# Holds all song attributes
from artist import Artist

class Song:
    def __init__ (self, song_id, title, artist: Artist, album, genre, file_path):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.file_path = file_path

        if album is not None:
            album.add_song(self)

        artist.add_song(self)

    def print_song(self):
        print(f"{self.title} - {self.artist} - {self.album} - {self.genre}")

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.album} - {self.genre}"
