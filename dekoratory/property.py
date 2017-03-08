class Data:
    def __init__(self):
        self.x, self.y = 0, 0
    @property
    def avg(self):
        """Read-only"""
        return (self.x + self.y) / 2

class User:
    def __init__(self):
        self._email = None
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, val):
        if "@" in val:
            self._email = val
        else:
            raise ValueError("Co to za mail bez małpy!")
