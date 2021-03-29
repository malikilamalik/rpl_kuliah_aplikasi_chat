class Grup:
    def __init__(self, id_grup, nama_grup, deskripsi_grup):
        self.id_grup = id_grup
        self.nama_grup = nama_grup
        self.deskripsi_grup = deskripsi_grup

    def MembuatGrup(self):
        msg = "Grup {} berhasil dibuat".format(self.nama_grup)
        return msg