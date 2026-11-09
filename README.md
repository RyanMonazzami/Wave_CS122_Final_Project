# Wave_CS122_Final_Project
## Quick Start
Run these commands from the project root. First, create and activate a Python virtual environment\
### MacOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
### Windows Powershell
```
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
### Install SQLAlchemy
```
python -m pip install SQLAlchemy
```

### Install the web app dependencies

With `.venv` active, run this from the project root.

```bash
python -m pip install Flask SQLAlchemy
```

### Set up the database and audio files

Run this once when creating a fresh `wave.db`.

```bash
python load_database.py
```

Put the MP3 files in `Songs/` using the filenames specified in `load_database.py`.

### Start the web app

```bash
flask --app api:app run --debug
```

Open [Wave in your browser](http://127.0.0.1:5000/).
