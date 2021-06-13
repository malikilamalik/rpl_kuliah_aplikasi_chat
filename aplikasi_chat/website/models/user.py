from website import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(255))
    tanggal_lahir = db.Column(db.Date)
    no_hp = db.Column(db.String(16))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()