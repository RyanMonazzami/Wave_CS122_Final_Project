# Holds all song attributes
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

    def print_song(self):
        print(f"{self.title} - {self.artist} - {self.album} - {self.genre}")

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.album} - {self.genre}"
