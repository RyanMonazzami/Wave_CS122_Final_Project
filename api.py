from flask import Flask, jsonify, request, send_file
from database import Session
from search import Library
from song import Song
from pathlib import Path
from album import Album
from artist import Artist
app = Flask(__name__)

@app.get("/")
@app.get("/artists/{artist_id}")
@app.get("/albums/{album_id}")
def show_page():
    return send_file(
        Path(__file__).with_name("index.html"),
        mimetype="text/html",
    )

@app.get("/songs")
def get_songs(q: str = ""):
    with Session() as session:
        library = Library()
        songs = session.query(Song).order_by(Song.song_id).all()

        for song in songs:
            library.add_song(song)

        matches = library.search_songs(q)
        return [
            {
                "song_id": song.song_id,
                "title": song.title,
                "artist": song.artist.name,
                "album": song.album.title,
            }
            for song in matches
        ]

@app.get("/songs/<song_id>/audio")
def get_audio_song(song_id: int):
    with Session() as session:
        song = session.query(Song).filter_by(song_id=song_id).first()

        if not song:
            raise jsonify(status_code=404, detail="Song not found.")

        file_path = Path(song.file_path)

        if file_path.is_file():
            return send_file(file_path, mimetype="audio/mpeg")
        else:
            raise jsonify(status_code=404, detail="File not found.")





