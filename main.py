from album import Album
from artist import Artist
from audio_player import AudioPlayer
from database import Session
from search import Library
from song import Song


def main ():
    library = Library()
    with Session() as session:

        songs = session.query(Song).all()

        for song in songs:
            library.add_song(song)

        matches = library.search_songs("I Couldn't Love You More")

        if not matches:
            print("No matches found.")
            return

        song = matches[0]


        print(f"Loaded {len(library.songs)} songs")


        player = AudioPlayer()
        try:
            player.play_song(song)
            print(f"Playing {song.title}")
            input("Press Enter to stop playback...")
        finally:
            player.close()

    session.close()

main()


