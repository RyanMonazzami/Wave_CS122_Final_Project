# Album object includes album attributes and stores collection of songs

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Album(Base):
    # Albums table
    __tablename__ = "albums"
    # Album attributes
    album_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artwork_filename = Column(String, nullable=True)
    artist_id = Column(Integer, ForeignKey("artists.artist_id"), nullable=False)
    release_date = Column(String)

    # Artist and song relationships
    # back_populates syncs relationships 
    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def get_songs(self):
        return self.songs

    def get_artist(self):
        return self.artist

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_album_id(self):
        return self.album_id

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
