# Holds all song attributes
from pathlib import Path

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Song(Base):
    # Song table
    __tablename__ = "songs"

    # Song attributes
    song_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.artist_id"), nullable=False)
    album_id = Column(Integer, ForeignKey("albums.album_id"), nullable=True)
    genre = Column(String, nullable=False)
    file_path = Column(String, nullable=False)

    # Artist and album relationships
    # back_populates syncs relationships
    artist = relationship("Artist", back_populates="songs")
    album = relationship("Album", back_populates="songs")

    @property
    def artwork_filename(self):
        album = self.album
        if album is None:
            return None

        return album.artwork_filename

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_file_path(self):
        return self.file_path

    def get_artist_name(self):
        return self.artist.name

    def get_album_title(self):
        if self.album is None:
            return "Single"
        return self.album.title

    # checks if the mp3 file exists
    def has_audio_file(self):
        return Path(self.file_path).is_file()

    def get_info(self):
        return f"{self.title} - {self.get_artist_name()} - {self.get_album_title()} - {self.genre}"

    def print_song(self):
        print(self.get_info())

    def __str__(self):
        return self.get_info()
