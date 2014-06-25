import unittest
import database


class database_tests(unittest.TestCase):

    def setUp(self):
        database.create_users_table()
        database.register('Barney', '420', "Mclarens")
        database.create_restaurant_table('speedy')
        database.add('speedy', 'pizza', 3.50)
        database.status('speedy', 'Not taking orders.')

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

    def test_add_existing_restaurant(self):
        self.assertFalse(database.create_restaurant_table('speedy'))

    def test_add_pizza_price(self):
        database.cursor.execute("SELECT price \
        FROM speedy WHERE products = 'pizza'")
        price = database.cursor.fetchone()

        self.assertEqual(3.50, price[0])

    def test_add_pizza_twice(self):
        self.assertFalse(database.add('speedy', 'pizza', 4.00))

    def test_is_open(self):
        self.assertFalse(database.open('speedy'))

    def test_close_an_open_restaurant(self):
        self.assertTrue(database.close('speedy'))

    def test_set_status(self):
        database.cursor.execute("SELECT status FROM speedy LIMIT 1")
        status = database.cursor.fetchone()
        self.assertEqual('Not taking orders.', status[0])

    def tearDown(self):
        database.cursor.execute('DROP TABLE users')
        database.cursor.execute('DROP TABLE speedy')

if __name__ == '__main__':
    unittest.main()
