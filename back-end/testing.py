from model.user import User

user1 = User("OKEI","malik", "secret123", "20-20-2020", "082219738808", "Laki Dong")

user2 = User("OKE2","ryan", "secret123", "20-10-1945", "082219738808", "Laki Banget")

print("Kirim Pesan")
print(user1.kirim_pesan())
print("Lihat Profil User")
print(user1.lihat_profil_user())
print("Lihat Profil User Teman")
print(user1.lihat_profil_user_teman(user2))