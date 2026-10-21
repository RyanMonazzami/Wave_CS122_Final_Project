from album import Album
from artist import Artist
from song import Song
from audio_player import AudioPlayer


def main ():
    kanye = Artist(1, "Kanye West")
    album = Album(1, "The College Dropout", kanye, "2-10-04")
    song = Song(1, "All Falls Down", kanye, album, "Hip-Hop", "Songs/Kanye_West_-_All_Falls_Down_-_feat._Sylena_Johnson.mp3")
    album.add_song(song)

    player = AudioPlayer()

    try:
        player.play_song(song)
        print(f"{song.title} is playing...")
        input("Press Enter to end playback")
        
    finally:
        player.close()

main()
