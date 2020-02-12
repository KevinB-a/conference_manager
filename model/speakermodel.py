from .connection import Connection

from .entities.speaker import Speaker


class SpeakerModel:
    """class to perform all queries in table speaker"""

    def __init__(self):
        """initialize arguments"""
        self.values = ()
        self.sql = ""
        self.db = Connection()

    def display_speaker(self):
        """select all speaker in table speaker"""
        self.sql = "SELECT * FROM speaker WHERE status = True;"
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql)
        speaker = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, values in enumerate(speaker):
            speaker[key] = Speaker(values)

    def add_speaker(self, last_name, first_name, description, job):
        """add new entry in table speaker"""
        self.sql = "INSERT INTO speaker(last_name, first_name, description, status, job) VALUES(%s, %s, %s, %s, %s);"
        self.values = (last_name, first_name, description, job)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()
        self.db.close_connection()

    def update_speaker(self, last_name, first_name, description, status, job, speaker_id):
        """update data in table speaker"""
        self.sql = "UPDATE speaker SET last_name = %s, first_name = %s, description = %s , status = %s, job = %s " \
                   "WHERE speaker_id = %s; "
        self.values = (last_name, first_name, description, status, job, speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_speaker(self, speaker_id):
        """delete data in table speaker"""
        self.sql = "DELETE FROM speaker WHERE speaker_id = %s;"
        self.values = (speaker_id,)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()
        self.db.close_connection()
