from .entities.id import Id


class Conference(Id):

    def __init__(self, data=False):
        """initialize attribute """
        super().__init__()
        self.conference_id = None
        self.title = None
        self.summary = None
        self.date = None
        self.hour = None
        self.creation_date = None
        if data:
            self.hydrate(data)

    def __str__(self):
        text = "{} information \n\
        summary : {} \n\
        date : {} \n\
        hour : {} \n\
        creation_date : {} \n\
        "
        print(text.format(self.title, self.summary, self.date, self.hour, self.creation_date))
