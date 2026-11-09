# Wave_CS122_Final_Project
Quick Start\
Run these commands from the project root. First, create and activate a Python virtual environment\
MacOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows Powershell
```
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Install SQLAlchemy
```
python -m pip install SQLAlchemy
```

Install the web app dependencies with .venv active.
```
python -m pip install fastapi uvicorn SQLAlchemy
```
Load the database
```
python load_database.py
```
Start the web app
```
python -m uvicorn api:app --reload
```
