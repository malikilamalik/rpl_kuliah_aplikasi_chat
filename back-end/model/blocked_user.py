class Blocked_user :

    def __init__(self,id,user_id):
        self.id =id
        self.id_user_blocked = user_id
    
    def blocked(self,user_id):
        pesan = "User id : {}\n blocked".format(self.user_id)
        return pesan

    