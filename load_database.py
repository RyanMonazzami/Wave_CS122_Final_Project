from database import Session, init_db, engine
from artist import Artist
from album import Album
from song import Song

# Create database
init_db()
with engine.connect() as connection:
    print(connection.exec_driver_sql("PRAGMA database_list").all())
# Start session
session = Session()

# Artists
kanye = Artist(artist_id=1, name="Kanye West")
sade = Artist(artist_id=2, name="Sade")

# Albums
tcd = Album(album_id=1, title="The College Dropout", artist_id=1, release_date="2-10-2004")
ld = Album(album_id=2, title="Love Deluxe", artist_id=2, release_date="10-26-1992")

# Songs
# Kanye
wdc = Song(song_id=1, title="We Don't Care", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/We Don't Care.mp3")
afd = Song(song_id=2, title="All Falls Down", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/All_Falls_Down.mp3")
ss = Song(song_id=3, title="Spaceships", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Spaceship.mp3")
jw = Song(song_id=4, title="Jesus Walks", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Jesus Walks.mp3")
nlmd = Song(song_id=5, title="Never Let Me Down", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Never Let Me Down.mp3")
sj = Song(song_id=6, title="Slow Jamz", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Slow Jamz.mp3")
tw = Song(song_id=7, title="Two Words", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Two Words.mp3")
ttw = Song(song_id=8, title="Through The Wire", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Through The Wire.mp3")
fb = Song(song_id=9, title="Family Business", artist_id=1, album_id=1, genre="Hip-Hop", file_path="Songs/Family Business.mp3")

# Sade
nod = Song(song_id=10, title="No Ordinary Love", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/No Ordinary Love.mp3")
fnp = Song(song_id=11, title="Feel No Pain", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Feel No Pain.mp3")
iclym = Song(song_id=12, title="I Couldn't Love You More", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/I Couldn't Love You More.mp3")
lat = Song(song_id=13, title="Like a Tattoo", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Like a Tattoo.mp3")
kol = Song(song_id=14, title="Kiss of Life", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Kiss of Life.mp3")
p = Song(song_id=15, title="Pearls", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Pearls.mp3")
ctd = Song(song_id=16, title="Cherish The Day", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Cherish The Day.mp3")
bfs = Song(song_id=17, title="Bullet Proof Soul", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Bulletproof Soul.mp3")
m = Song(song_id=18, title="Mermaid", artist_id=2, album_id=2, genre="R&B/Soul", file_path="Songs/Mermaid.mp3")

session.add_all([kanye, sade, tcd, ld, wdc, afd, ss, jw, nlmd, sj, tw, ttw, fb, nod, fnp, iclym, lat, kol, p, ctd, bfs, m])
session.commit()
session.close()