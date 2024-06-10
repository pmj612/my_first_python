class MyIterable:
    def __init__(self, values):
        self._values = values

    def __iter__(self):
        #return None  # Noncompliant: Not a valid iterator..
