from website import db

class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(16))
    description = db.Column(db.String())

    def create(self):
        db.session.add(self)
        db.session.commit()