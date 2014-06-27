class user:
    def __init__(self, username, address):
        self._username = username
        self._address = address
        self._basket = []

    def get_username(self):
        return self._username

    def get_address(self):
        return self._address

    def get_basket(self):
        return self._basket

    def set_address(self, new_address):
        self._address = new_address

    def set_basket(self, new_basket):
        self._basket = new_basket
