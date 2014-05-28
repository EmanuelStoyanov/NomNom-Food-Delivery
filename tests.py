import unittest
import Database


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        Database.create_users_table()
        Database.register('Barney', '420', "Mclarens")

    def test_admin(self):
        Database.cursor.execute("SELECT username, password \
            FROM users WHERE username = 'admin'")
        admin = Database.cursor.fetchone()

        self.assertEqual(admin[0], 'admin')
        self.assertEqual(admin[1], 'ADMINNOMNOM')

    def test_register_username(self):
        Database.cursor.execute('SELECT username FROM users \
        WHERE username = (?) AND password = (?)', ('Barney', '420'))
        username = Database.cursor.fetchone()

        self.assertEqual(username[0], 'Barney')

    def test_register_address(self):
        Database.cursor.execute('SELECT address FROM users \
        WHERE username = (?) AND password = (?)', ('Barney', '420'))
        username = Database.cursor.fetchone()

        self.assertEqual(username[0], 'Mclarens')

    def test_login(self):
        logged_user = Database.login('Barney', '420')
        self.assertEqual(logged_user.get_username(), 'Barney')

    def test_login_wrong_password(self):
        logged_user = Database.login('Barney', '421')
        self.assertFalse(logged_user)

    def tearDown(self):
        Database.cursor.execute('DROP TABLE users')

if __name__ == '__main__':
    unittest.main()
