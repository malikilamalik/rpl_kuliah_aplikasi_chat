class User:

    def __init__(self, id, username, password, tanggal_lahir, no_hp, jenis_kelamin):
        self.id = id
        self.username = username
        self.password = password
        self.tanggal_lahir = tanggal_lahir
        self.no_hp = no_hp
        self.jenis_kelamin = jenis_kelamin
    
    def kirim_pesan(self):
        input_pesan = input("Isi Pesan : ")
        pesan = "{} : {}".format(self.username, input_pesan)
        return pesan
    
    def tambah_teman(self, user):
        pesan = "{} menambahkan {} sebagai teman".format(self.username, user.username)
        return se

    def lihat_profil_user(self):
        pesan = "Username : {}\nTanggal lahir :{}\nNomor handphone : {}\nJenis kelamin : {}".format(self.username, self.tanggal_lahir, self.no_hp, self.jenis_kelamin)
        return pesan

    def lihat_profil_user_teman(self,user):
        pesan = "Username : {}\nTanggal lahir :{}\nNomor handphone : {}\nJenis kelamin : {}".format(user.username, user.tanggal_lahir, user.no_hp, user.jenis_kelamin)
        return pesan