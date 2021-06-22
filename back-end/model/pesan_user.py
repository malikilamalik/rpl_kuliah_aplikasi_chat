class Pesan_User():
    def __init__(self, id_pesan, isi_pesan, sender, receiver):
        self.id_pesan = id_pesan
        self.isi_pesan = isi_pesan
        self.sender = sender
        self.receiver = receiver

    def sendPesan_User(self, listPesan):
        listPesan[(self.id_pesan, self.sender, self.receiver)] = self.isi_pesan
        print('Pesan terkirim ke {}'.format(self.receiver))

    def showPesan_User(self, receiver, listPesan):
        print(self.sender,' :')
        print()
