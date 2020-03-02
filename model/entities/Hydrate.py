class Hydrate:
    """class hydrate """
    def __init__(self):
        self.conference_id = None
        self.title = None
        self.summary = None
        self.date = None
        self.hour = None
        self.creation_date = None
        self.speaker_id = None
        self.last_name = None
        self.first_name = None
        self.description = None
        self.status = None
        self.job = None

    def hydrate(self, data):
        """Set object's attribute value if they exists from a dictionary """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
