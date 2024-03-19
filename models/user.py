class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def to_json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}