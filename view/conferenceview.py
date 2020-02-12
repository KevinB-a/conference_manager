from model.conferencemodel import ConferenceModel


class ConferenceView:
    """class to retrieve conference model info """

    def __init__(self):
        self.model = ConferenceModel()

    def show_conferences(self):
        """display all conferences with two fields from speaker"""
        print("Bonjour voici la liste des conferences")
        self.model.display_conferences()

    def new_conference(self):
        """Displays inputs to register a new speaker in table speaker"""
        title = input("Entrez le titre de la conference :")
        summary = input("Entrez le resume de la conference :")
        date = input("Entrez la date de la conference :")
        hour = input("Entrez l'heure de la conference :")
        self.model.add_conference(title, summary, date, hour)

    def to_update_conference(self):
        """display input to modify a new speaker in table speaker """
        title = input("Entrez le titre de la conference :")
        summary = input("Entrez le resume de la conference :")
        date = input("Entrez la date de la conference :")
        hour = input("Entrez l'heure de la conference :")
        conference_id = int(input("Entrez l'id de la conference"))
        self.model.update_conference(title, summary, date, hour, conference_id)

    def remove_conference(self):
        """display inputs to delete conference in table conference"""
        conference_id = int(input("Entrez l'id de la conference :"))
        self.model.delete_conference(conference_id)
