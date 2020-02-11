class Id:

    def __init__(self):
        self.id = None

    def hydrate(self, data):
        """Set object's attribute value if they exists from a dictionary """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
