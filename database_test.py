from database import Session, init_db
from artist import Artist
from album import Album
from song import Song

# Create database
init_db()
# Start session
session = Session()

file_path = "Songs/Kanye_West_-_All_Falls_Down_-_feat._Sylena_Johnson.mp3"

# Query for song from database or None if no song exists
song = session.query(Song).filter(Song.file_path == file_path).first()

# If song does not exist build and add it
if song is None:
    kanye = Artist(name="Kanye West")

    tcd = Album(title="The College Dropout", artist=kanye, release_date="2-10-2004")

    song = Song(title="All Falls Down", artist=kanye, album=tcd, genre="Hip-Hop", file_path=file_path)

    # Add song to session
    session.add(song)
    # Save session changes
    session.commit()
    print("Saved new song")
else:
    print("Loaded song")

# Print song information
print("Song ID:", song.song_id)
print("Title:", song.title)
print("Artist:", song.artist.name)
print("Album:", song.album.title)

# Close session
session.close()