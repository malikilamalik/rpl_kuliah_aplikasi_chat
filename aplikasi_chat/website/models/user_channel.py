from website import db

class UserGroup(db.Model):
    __tablename__ = 'user_groups'
    id = db.Column(db.String(255), primary_key=True)
    id_user = db.Column(db.String(255))
    id_channel = db.Column(db.String(255))
    role = db.Column(db.Enum('admin','user'))

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()