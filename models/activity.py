class Activity:
    def __init__(self, id, name, description, duration, date, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration
        self.date = date
        self.user_id = user_id

    def to_json(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'duration': self.duration,
                'date': self.date,
                'user_id': self.user_id
                }
