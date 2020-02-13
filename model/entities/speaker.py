from .Hydrate import Hydrate


class Speaker(Hydrate):

    def __init__(self, data):
        """initialize attribute"""
        super().__init__()
        if data:
            self.hydrate(data)

    def __str__(self):
        return """~~~~~~~~~~~~~~~~~~~~~~~~
last_name : {} \n\
first_name : {} \n\
description : {} \n\
status: {} \n\
job : {}
~~~~~~~~~~~~~~~~~~~~~~~~

        """.format(self.last_name, self.first_name, self.description, self.status, self.job)
