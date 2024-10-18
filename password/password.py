
class Password:
    def __init__(self, password, length=8):
        self.password = password
        self.lenght = length


    def is_strong(self):
        return len(self.password) >= 6


    def change_password(self, new_password):
        self.password = new_password
