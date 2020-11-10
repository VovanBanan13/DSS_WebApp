from app import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    temperature = db.Column(db.Integer)

    def __repr__(self):
        return '<Region {}>'.format(self.name)