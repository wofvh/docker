class User(object):
    def __init__(self,id,password):
        self.id = id
        self.password = password
        
    def get_id(self):
        return self.id
    
    def get_password(self):
        return self.password