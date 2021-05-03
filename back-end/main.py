#Import class grup.py dari direktori ../model/grup
from model.grup import Grup

#Inisiasi list/array untuk menyimpan semua grup yang akan dibuat
ListGrup = []

#Inisiasi semua objek Grup dengan parameter Grup(id_grup, nama_grup, deskripsi_grup) dengan memanggil konstruktor dari class grup.py
Grup1 = Grup("001", "Kelompok 02 RPL", "Grup untuk Diskusi Project RPL Aplikasi Chat Kelompok 02")
Grup2 = Grup("002", "IF-42-02", "Grup Umum Kelas IF-42-02")
Grup3 = Grup("003", "Informatika18", "Grup Umum untuk Mahasiswa Informatika Angkatan 2018")

#Append/daftarkan semua objek Grup yang telah diinisiasi ke dalam ListGrup
ListGrup.append(Grup1)
ListGrup.append(Grup2)
ListGrup.append(Grup3)

#Outputkan semua objek Grup yang telah disimpan dalam ListGrup
for group in ListGrup:
    print(group.MembuatGrup())
