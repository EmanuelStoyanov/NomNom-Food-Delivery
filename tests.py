import unittest
import database


class database_tests(unittest.TestCase):

    def setUp(self):
        database.create_users_table()
        database.create_restaurant_table()
        database.create_orders_table()
        database.create_taxes_table()
        database.register('Barney', '420', "Mclarens")
        database.create_menu_table('speedy')
        database.create_menu_table('subway')
        database.add('speedy', 'pizza', 3.50)
        database.status_r('speedy', 'Not taking orders.')


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
        database.cursor.execute('DROP TABLE speedy')
        database.cursor.execute('DROP TABLE restaurants')
        database.cursor.execute('DROP TABLE subway')
        database.cursor.execute('DROP table orders')
        database.cursor.execute('DROP table taxes')

    def test_add_existing_restaurant(self):
        self.assertFalse(database.create_menu_table('speedy'))

    def test_add_pizza_price(self):
        database.cursor.execute("SELECT price \
        FROM speedy WHERE products = 'pizza'")
        price = database.cursor.fetchone()

        self.assertEqual(3.50, price[0])

    def test_add_pizza_twice(self):
        self.assertFalse(database.add('speedy', 'pizza', 4.00))

    def test_close_a_closed_restaurant(self):
        self.assertFalse(database.close('speedy'))

    def test_open_closed_restaurant(self):
        self.assertTrue(database.open('speedy'))

    def test_open_an_opened_restaurant(self):
        database.open('subway')
        self.assertFalse(database.open('subway'))

    def test_close_an_open_restaurant(self):
        database.open('subway')
        self.assertTrue(database.close('subway'))

    def test_set_status(self):
        database.cursor.execute("SELECT status \
        FROM restaurants WHERE name = 'speedy'")
        status = database.cursor.fetchone()
        self.assertEqual('Not taking orders.', status[0])


if __name__ == '__main__':
    unittest.main()
