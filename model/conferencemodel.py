from .connection import Connection

from .entities.conference import Conference


class ConferenceModel:
    """class to perform all queries in table conference"""

    def __init__(self):
        self.values = ()
        self.sql = ""
        self.db = Connection()

    def display_conferences(self):
        """select all conference from conference and add last name and first name from speaker """
        # self.sql = "SELECT c.*, s.last_name, s.first_name FROM conference AS c LEFT JOIN speaker AS s ON c.speaker_id =s.speaker_id; "
        self.sql = """SELECT c.*, s.last_name, s.first_name FROM conference AS c
        INNER JOIN speaker AS s
        ON s.speaker_id = c.speaker_id
        ORDER BY c.date, c.hour;"""  # query for display all data in table conference with two fields from speaker
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql)
        conference = self.db.cursor.fetchall()  # display every conference
        self.db.close_connection()
        for key, value in enumerate(conference):
            conference[key] = Conference(value)
        return conference

    def add_conference(self, title, summary, date, hour, speaker_id):
        """add new entry in table conference"""
        self.sql = "INSERT INTO conference(title, summary, date, hour, creation_date, speaker_id) VALUES(%s, %s, %s, %s, now(),%s);"  # query for add new data
        self.values = (title, summary, date, hour, speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()  # method to save the new entry
        self.db.close_connection()

    def update_conference(self, title, summary, date, hour, conference_id):
        """update data in table conference"""
        self.sql = "UPDATE conference SET title = %s, summary = %s, date = %s, hour = %s WHERE conference_id =%s;"  # query for update one data
        self.values = (title, summary, date, hour, conference_id)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()  # save update
        self.db.close_connection()

    def delete_conference(self, conference_id):
        """delete data in table conference"""
        self.sql = "DELETE FROM conference WHERE conference_id = %s;"  # query for delete data
        self.values = (conference_id,)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, (self.values,))
        self.db.connection.commit()  # save delete
        self.db.close_connection()
