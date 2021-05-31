from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Inisiasi class Grup yang berisi beberapa method/function
class Grup(db.Model):
    __tablename__ = 'grup'
    id_grup = db.Column(db.Integer, primary_key=True)
    nama_grup = db.Column(db.String)
    deskripsi_grup = db.Column(db.String)

    #Constructor method untuk class Grup itu sendiri dengan parameter id_grup, nama_grup, dan deskripsi_grup
    def __init__(self, id_grup, nama_grup, deskripsi_grup):
        self.id_grup = id_grup
        self.nama_grup = nama_grup
        self.deskripsi_grup = deskripsi_grup

    #Method untuk mengoutputkan pesan bahwa Grup berhasil dinisiasi/dibuat
    def MembuatGrup(self):
        msg = "Grup {} berhasil dibuat".format(self.nama_grup)
        return msg