# Artist object that contains artist attributes alongside collection of albums and singles


class Artist:
    def __init__(self, artist_id, name):
        self.artist_id = artist_id
        self.name = name

        self.albums = []
        self.songs = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def get_albums(self):
        return self.albums

    def get_songs(self):
        return self.songs

    def __str__(self):
        return f"{self.artist_id}, {self.name}"
