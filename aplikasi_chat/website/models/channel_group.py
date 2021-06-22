from website import db

class ChannelGroup(db.Model):
    __tablename__ = 'channel_groups'
    id = db.Column(db.String(255), primary_key=True)
    id_group = db.Column(db.String(255))
    id_channel = db.Column(db.String(255))

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()