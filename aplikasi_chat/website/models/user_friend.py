from website import db

class UserFriend(db.Model):
    __tablename__ = 'user_friends'
    id = db.Column(db.String(255), primary_key=True)
    id_user = db.Column(db.String(255))
    id_user_teman = db.Column(db.String(255))
    user_room = db.Column(db.String(255))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()