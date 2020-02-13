from model.speakermodel import SpeakerModel


class SpeakerView:
    """class to retrieve speaker model info"""

    def __init__(self):
        self.model = SpeakerModel()

    def show_speakers(self):
        """display all speakers"""
        print("Bonjour voici la liste des conferenciers ")
        speakers = self.model.display_speaker()
        if speakers:
            for speaker in speakers:
                print(speaker)

    def new_speaker(self):
        """Displays inputs to register a new speaker in table speaker"""
        last_name = input("Entrez le nom de famille :")
        first_name = input("Entrez le prenom :")
        description = input("Entrez une description")
        job = input("Entrez la profession")
        self.model.add_speaker(last_name, first_name, description, job)

    def to_update_speaker(self):
        """display input to modify a new speaker in table speaker"""
        last_name = input("Entrez le nom de famille :")
        first_name = input("Entrez le prenom :")
        description = input("Entrez une description:")
        job = input("Entrez la profession :")
        speaker_id = int(input("Entrez l'id du speaker :"))
        self.model.update_speaker(last_name, first_name, description, job, speaker_id)

    def remove_speaker(self):
        """display inputs to delete speaker in table speaker"""
        speaker_id = input("Entrez l'id du conferencier :")
        self.model.delete_speaker(speaker_id)
