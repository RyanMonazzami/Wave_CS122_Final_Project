# Playlist object holds an ordered list of songs, PlaylistManager handles creating and managing playlists


class Playlist:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.songs = []

    def add_song(self, song):
        if song in self.songs:
            return False
        self.songs.append(song)
        return True

    def remove_song(self, song):
        if song not in self.songs:
            return False
        self.songs.remove(song)
        return True

    def move_song(self, old_index, new_index):
        if not (0 <= old_index < len(self.songs)) or not (0 <= new_index < len(self.songs)):
            return False
        song = self.songs.pop(old_index)
        self.songs.insert(new_index, song)
        return True

    def rename(self, new_name):
        self.name = new_name

    def clear(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"{self.name} ({len(self.songs)} songs)"


class PlaylistManager:
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name, description=""):
        if name in self.playlists:
            return None
        playlist = Playlist(name, description)
        self.playlists[name] = playlist
        return playlist

    def delete_playlist(self, name):
        return self.playlists.pop(name, None) is not None

    def get_playlist(self, name):
        return self.playlists.get(name)

    def rename_playlist(self, old_name, new_name):
        if old_name not in self.playlists or new_name in self.playlists:
            return False
        playlist = self.playlists.pop(old_name)
        playlist.rename(new_name)
        self.playlists[new_name] = playlist
        return True

    def list_playlists(self):
        return list(self.playlists.values())
