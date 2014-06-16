class user:
    def __init__(self, username, address):
        self.username = username
        self.address = address
        self.basket = []

    def get_username(self):
        return self.username

    def get_adress(self):
        return self.address
