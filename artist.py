# Artist object that contains artist attributes alongside collection of albums and singles
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Artist(Base):
    # Artists table
    __tablename__ = 'artists'

    # Artist attributes
    artist_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Albums and songs that belong to artist
    # back_populates syncs relationships
    albums = relationship("Album", back_populates="artist")
    songs = relationship("Song", back_populates="artist")

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
