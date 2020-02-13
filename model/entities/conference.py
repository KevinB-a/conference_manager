from .Hydrate import Hydrate


class Conference(Hydrate):
    """class representing the conference entity"""

    def __init__(self, data=False):
        """initialize attribute """
        super().__init__()
        if data:
            self.hydrate(data)

    def __str__(self):
        return """~~~~~~~~~~~~~~~~~~~~~~~~
title : {} \n\
summary : {} \n\
date : {} \n\
hour : {} \n\
creation_date : {} \n\
last_name : {} \n\
first_name : {} \n\
speaker_id : {} \n\
~~~~~~~~~~~~~~~~~~~~~~~~       
        """.format(self.title, self.summary, self.date, self.hour,self.creation_date,  self.last_name, self.first_name, self.speaker_id)
