from model.conferencemodel import ConferenceModel


class ConferenceView:
    """class to retrieve conference model info """

    def __init__(self):
        self.model = ConferenceModel()

    def show_conferences(self):
        """display all conferences with two fields from speaker"""
        print("Bonjour voici la liste des conferences")
        conferences = self.model.display_conferences()  # the variable conference recover data from method display_conference
        if conferences:  # if conferences exists
            for conference in conferences:
                print(conference)  # display every conference in conferences
        else:
            print("Pas de conference dans la base de donnees")

    def new_conference(self):
        """Displays inputs to register a new speaker in table speaker"""
        title = input("Entrez le titre de la conference :")
        summary = input("Entrez le resume de la conference :")
        date = input("Entrez la date de la conference (aaaa/mm/jj) :")
        hour = input("Entrez l'heure de la conference (hh:mm) :")
        speaker_id = int(input("Entrez l'id du conférencier :"))
        self.model.add_conference(title, summary, date, hour, speaker_id)

    def to_update_conference(self):
        """display input to modify a new speaker in table speaker """
        title = input("Entrez le titre de la conference :")
        summary = input("Entrez le resume de la conference :")
        date = input("Entrez la date de la conference (aaaa/mm/jj):")
        hour = input("Entrez l'heure de la conference (hh:mm):")
        conference_id = int(input("Entrez l'id de la conference"))
        self.model.update_conference(title, summary, date, hour, conference_id)

    def remove_conference(self):
        """display inputs to delete conference in table conference"""
        conference_id = int(input("Entrez l'id de la conference :"))
        self.model.delete_conference(conference_id)
