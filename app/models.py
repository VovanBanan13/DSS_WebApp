from app import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    duration = db.Column(db.Integer)
    temperature = db.Column(db.Float)  

    def __repr__(self):
        return '<Регион: {}, температура {}, продолжительность {}>'.format(self.name, self.temperature, self.duration)

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    thermal = db.Column(db.Float)
    depth = db.Column(db.Float)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Материал: {}, теплопроводность {}, толщина {}, цена {}>'.format(self.name, self.thermal, self.depth, self.price)
