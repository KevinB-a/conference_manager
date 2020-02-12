from .id import Id


class Speaker(Id):

    def __init__(self, data):
        """initialize attribute"""
        super().__init__()
        self.speaker_id = None
        self.last_name = None
        self.first_name = None
        self.description = None
        self.status = None
        self.job = None
        if data:
            self.hydrate(data)

    def __str__(self):
        text = "{} {} information \n\
        description : {} \n\
        status : {} \n\
        job : {} \n\
        "
        print(text.format(self.last_name, self.first_name, self.description, self.status, self.job))
