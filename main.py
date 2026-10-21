from album import Album
from artist import Artist
from song import Song


def main ():
    kanye = Artist("Kanye West", 1)
    album = Album("The College Dropout", 1, kanye, "2-10-04")
    song = Song(1, "All Falls Down", kanye, album, "Hip-Hop", "Songs/Kanye_West_-_All_Falls_Down_-_feat._Sylena_Johnson.mp3")
    album.add_song(song)