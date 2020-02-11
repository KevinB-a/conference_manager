from .connection import Connection

from .speaker import Speaker

class SpeakerModel:
    """"""

    def __init__(self):
        """initialize arguments"""
        self.sql = ""
        self.db = Connection()

    def display_speaker(self):
        """"""
        self.sql = "SELECT * FROM speaker;"
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql)
        speaker = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, values in enumerate(speaker):
            speaker[key] = Speaker(values)
