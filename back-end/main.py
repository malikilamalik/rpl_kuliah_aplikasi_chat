#IMPLEMENTASI USER
from model.user import User

#Inisiasi user "malik"
user1 = User("OKEI","malik", "secret123", "20-20-2020", "082219738808", "Laki Dong")
#Inisiasi user "ryan"
user2 = User("OKE2","ryan", "secret123", "20-10-1945", "082219738808", "Laki Banget")
#Inisiasi user "stevan"
user3 = User("OKE3","stevan", "secret123", "20-10-1945", "082219738808", "Laki-Laki")

print("Kirim Pesan")
print(user1.kirim_pesan())
print("Lihat Profil User")
print(user1.lihat_profil_user())
print("Lihat Profil User Teman")
print(user1.lihat_profil_user_teman(user2))

#IMPLEMENTASI BLOCK USER
#Import class Blocked_user dari direktori ../model/blocked_user
from model.blocked_user import Blocked_user
#Inisiasi list blocked user untuk user "malik"
list_blocked_user1 = Blocked_user("malik")
#Block username "stevan" dan tambahkan ke dalam list blocked user "malik"
list_blocked_user1.addToBlockedList("stevan")
print(list_blocked_user1.showBlocked("stevan"))
#Block username "ryan" dan tambahkan ke dalam list blocked user "malik"
list_blocked_user1.addToBlockedList("ryan")
print(list_blocked_user1.showBlocked("ryan"))

#Tampilkan isi list blocked user "malik"
print(list_blocked_user1.username,"'s Blocked User List :")
for i in range(len(list_blocked_user1.list_blocked)):
    print(i+1,")",list_blocked_user1.list_blocked[i])

#IMPLEMENTASI GRUP
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
