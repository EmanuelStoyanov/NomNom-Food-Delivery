import unittest
import database


class database_tests(unittest.TestCase):

    def setUp(self):
        database.create_users_table()
        database.register('Barney', '420', "Mclarens")

    def test_admin(self):
        database.cursor.execute("SELECT username, password \
            FROM users WHERE username = 'admin'")
        admin = database.cursor.fetchone()

        self.assertEqual(admin[0], 'admin')
        self.assertEqual(admin[1], 'ADMINNOMNOM')

    def test_register_username(self):
        database.cursor.execute('SELECT username FROM users \
        WHERE username = (?) AND password = (?)', ('Barney', '420'))
        username = database.cursor.fetchone()

        self.assertEqual(username[0], 'Barney')

    def test_register_address(self):
        database.cursor.execute('SELECT address FROM users \
        WHERE username = (?) AND password = (?)', ('Barney', '420'))
        username = database.cursor.fetchone()

        self.assertEqual(username[0], 'Mclarens')

    def test_login(self):
        logged_user = database.login('Barney', '420')
        self.assertEqual(logged_user.get_username(), 'Barney')

    def test_login_wrong_password(self):
        logged_user = database.login('Barney', '421')
        self.assertFalse(logged_user)

    def tearDown(self):
        database.cursor.execute('DROP TABLE users')

if __name__ == '__main__':
    unittest.main()
