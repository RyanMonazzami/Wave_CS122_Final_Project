from pathlib import Path
import pygame as pg
class AudioPlayer:
    def __init__(self):
        pg.mixer.init()
        pg.mixer.music.set_volume(0.1)

    def play_song(self, song):
        audio_path = Path(song.file_path)

        if not audio_path.is_file():
            raise FileNotFoundError(f"File not found at {audio_path}")

        pg.mixer.music.load(str(audio_path))
        pg.mixer.music.play()

    def pause(self):
        pg.mixer.music.pause()

    def resume(self):
        pg.mixer.music.unpause()

    def close(self):
        pg.mixer.music.stop()
        pg.mixer.quit()
