from app import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    temperature = db.Column(db.Integer)
    duration = db.Column(db.Integer)

    def __repr__(self):
        return '<Region {}>'.format(self.name)

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    thermal = db.Column(db.Integer)
    depth = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __repr__(self):
        return '<Material {}>'.format(self.name)