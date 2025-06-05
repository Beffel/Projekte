import os
import sqlite3
from tkinter import Tk, Frame, Label, Entry, Button, Listbox, Scrollbar, END, filedialog, StringVar

DB_FILE = 'music.db'

AUDIO_EXTS = ['.mp3', '.wav', '.flac', '.ogg', '.aiff']


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE,
            artist TEXT,
            length TEXT,
            key TEXT,
            date_added TEXT,
            date_produced TEXT,
            file_size INTEGER,
            file_type TEXT,
            energy TEXT,
            genre TEXT
        )"""
    )
    conn.commit()
    conn.close()


class MusicSorter(Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Sorter")

        self.dir_path = StringVar()

        self.create_widgets()

    def create_widgets(self):
        top_frame = Frame(self)
        top_frame.pack(padx=10, pady=10, fill='x')

        Label(top_frame, text="Music Directory:").pack(side='left')
        Entry(top_frame, textvariable=self.dir_path, width=40).pack(side='left', padx=5)
        Button(top_frame, text="Browse", command=self.browse_dir).pack(side='left')
        Button(top_frame, text="Load", command=self.load_files).pack(side='left', padx=5)

        mid_frame = Frame(self)
        mid_frame.pack(padx=10, pady=10, fill='both', expand=True)

        self.listbox = Listbox(mid_frame)
        self.listbox.pack(side='left', fill='both', expand=True)
        scrollbar = Scrollbar(mid_frame, command=self.listbox.yview)
        scrollbar.pack(side='left', fill='y')
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        form_frame = Frame(self)
        form_frame.pack(padx=10, pady=10)

        labels = [
            'Artist', 'Length', 'Key', 'Date Added', 'Date Produced',
            'File Size', 'File Type', 'Energy', 'Genre'
        ]
        self.entries = {}
        for idx, text in enumerate(labels):
            Label(form_frame, text=text).grid(row=idx, column=0, sticky='e')
            entry = Entry(form_frame, width=40)
            entry.grid(row=idx, column=1, padx=5, pady=2)
            self.entries[text] = entry

        Button(form_frame, text="Save Metadata", command=self.save_metadata).grid(
            row=len(labels), column=0, columnspan=2, pady=5
        )

    def browse_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_path.set(directory)

    def load_files(self):
        self.listbox.delete(0, END)
        directory = self.dir_path.get()
        if not directory:
            return
        for root, _, files in os.walk(directory):
            for f in files:
                if os.path.splitext(f)[1].lower() in AUDIO_EXTS:
                    self.listbox.insert(END, os.path.join(root, f))

    def on_select(self, event):
        selection = event.widget.curselection()
        if not selection:
            return
        index = selection[0]
        path = event.widget.get(index)
        self.load_metadata(path)

    def load_metadata(self, path):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT artist, length, key, date_added, date_produced, file_size, file_type, energy, genre FROM tracks WHERE path=?", (path,))
        row = c.fetchone()
        conn.close()
        labels = list(self.entries.keys())
        if row:
            for value, label in zip(row, labels):
                self.entries[label].delete(0, END)
                if value is not None:
                    self.entries[label].insert(0, str(value))
        else:
            for label in labels:
                self.entries[label].delete(0, END)
        self.current_path = path

    def save_metadata(self):
        if not hasattr(self, 'current_path'):
            return
        path = self.current_path
        data = [self.entries[label].get() or None for label in self.entries]
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        file_size = os.path.getsize(path)
        file_type = os.path.splitext(path)[1]
        c.execute(
            """INSERT INTO tracks (path, artist, length, key, date_added, date_produced, file_size, file_type, energy, genre)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
               ON CONFLICT(path) DO UPDATE SET
                   artist=excluded.artist,
                   length=excluded.length,
                   key=excluded.key,
                   date_added=excluded.date_added,
                   date_produced=excluded.date_produced,
                   file_size=excluded.file_size,
                   file_type=excluded.file_type,
                   energy=excluded.energy,
                   genre=excluded.genre""",
            (path, data[0], data[1], data[2], data[3], data[4], file_size, file_type, data[7], data[8])
        )
        conn.commit()
        conn.close()


def main():
    init_db()
    app = MusicSorter()
    app.mainloop()


if __name__ == '__main__':
    main()
