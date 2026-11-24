from flask import Flask, jsonify, request, send_file, render_template, abort

import album
from database import Session
from search import Library
from song import Song
from pathlib import Path
from album import Album
from artist import Artist
app = Flask(__name__)

@app.get("/")
def index():
    with Session() as session:
        artists = session.query(Artist).order_by(Artist.name).all()
    return render_template("index.html", artists=artists)

@app.get("/artists/<int:artist_id>")
def artist_page(artist_id: int):
    with Session() as session:
        artist = session.get(Artist, artist_id)
        if not artist:
            abort(404)

        return render_template("artist.html", artist=artist, albums=artist.albums)


@app.get("/albums/<int:album_id>")
def album_page(album_id: int):
    with Session() as session:
        album = session.get(Album, album_id)
        if not album:
            abort(404)

        return render_template("album.html", album=album, songs=album.songs)

@app.get("/search")
def search_page():
    # get the search text and genre from the url
    query = request.args.get("q", "")
    genre = request.args.get("genre", "")

    with Session() as session:
        library = Library()
        songs = session.query(Song).order_by(Song.song_id).all()

        for song in songs:
            library.add_song(song)

        genres = library.get_genres()

        song_results = []
        album_results = []
        artist_results = []

        if query or genre:
            song_results = library.filter_songs(title=query, genre=genre)

            if query:
                album_results = library.search_albums(query)
                artist_results = library.search_artists(query)

        return render_template("search.html", query=query, genre=genre, genres=genres,
                               songs=song_results, albums=album_results, artists=artist_results)

@app.get("/songs")
def get_songs(q: str = ""):
    # flask doesn't pass q in automatically so get it from the url
    q = request.args.get("q", q)
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
            abort(404, "Song not found.")

        file_path = Path(song.file_path)

        if file_path.is_file():
            return send_file(file_path, mimetype="audio/mpeg")
        else:
            abort(404, "File not found.")





