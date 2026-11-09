from album import Album
from artist import Artist
from audio_player import AudioPlayer
from database import Session
from song import Song


def main ():
    with Session() as session:
        song = session.query(Song).filter_by(song_id=12).first()

        player = AudioPlayer()
        try:
            player.play_song(song)
            print(f"Playing {song.title}")
            input("Press Enter to stop playback...")
        finally:
            player.close()

    session.close()

main()


