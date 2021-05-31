#Inisiasi class Blocked User yang berisi beberapa method/function
class Blocked_user() :
    #Self Constructor untuk Blocked User bersama atribut-atributnya
    def __init__(self, username):
        self.username = username
        self.list_blocked = []
    
    #Method untuk add/append username target yang ingin di-block ke list blocked user terkait
    def addToBlockedList(self, username):
        self.list_blocked.append(username)

    #Method untuk menampilkan pesan username target telah diblock oleh user
    def showBlocked(self, username):
        pesan = "Username {} blocked by {}".format(username,self.username)
        return pesan

    