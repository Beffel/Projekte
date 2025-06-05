# Music Sorter

This project provides a simple GUI application for organizing music files. It allows you to choose a directory containing your tracks and store custom metadata for each file in a small SQLite database.

## Features
- Select a directory and list all audio files (mp3, wav, flac, ogg, aiff).
- View and edit metadata fields such as artist, length, key, dates, energy and genre.
- Save metadata to an SQLite database so it persists between sessions.

## Requirements
The application relies on Python's standard library, including `tkinter` for the graphical user interface and `sqlite3` for the database. These modules are typically available by default in standard Python installations.

## Running
Change into the project directory and execute the script:

```bash
python music_sorter.py
```

Select your music directory, choose a file from the list and enter any metadata you wish to store. Press **Save Metadata** to store the information in `music.db`.
