from .Hydrate import Hydrate


class Conference(Hydrate):
    """class representing the conference entity"""

    def __init__(self, data=False):
        """initialize attribute """
        super().__init__()
        if data:   # if data == True execute hydrate method
            self.hydrate(data)

    def __str__(self):
        """method to display every information in table conference and last_name , first_name from speaker"""
        # display information this way
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
