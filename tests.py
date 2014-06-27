import unittest
import database
import logged_menu

class database_tests(unittest.TestCase):

    def setUp(self):
        database.create_users_table()
        database.create_restaurant_table()
        database.create_orders_table()
        database.create_taxes_table()
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

    def test_add_existing_restaurant(self):
        database.create_menu_table('speedy')
        self.assertFalse(database.create_menu_table('speedy'))

    def test_add_pizza_price(self):
        database.create_menu_table('speedy')
        database.add('speedy', 'pizza', 3.50)
        database.cursor.execute("SELECT price \
        FROM speedy WHERE products = 'pizza'")
        price = database.cursor.fetchone()

        self.assertEqual(3.50, price[0])

    def test_add_pizza_twice(self):
        database.create_menu_table('speedy')
        database.add('speedy', 'pizza', 3.50)
        self.assertFalse(database.add('speedy', 'pizza', 4.00))

    def test_close_a_closed_restaurant(self):
        database.create_menu_table('speedy')
        self.assertFalse(database.close('speedy'))

    def test_open_closed_restaurant(self):
        database.create_menu_table('speedy')
        self.assertTrue(database.open('speedy'))

    def test_open_an_opened_restaurant(self):
        database.create_menu_table('subway')
        database.open('subway')
        self.assertFalse(database.open('subway'))

    def test_close_an_open_restaurant(self):
        database.create_menu_table('subway')
        database.open('subway')
        self.assertTrue(database.close('subway'))

    def test_set_status(self):
        database.create_menu_table('speedy')
        database.update_status_restaurant('speedy', 'Not taking orders.')
        database.cursor.execute("SELECT status \
        FROM restaurants WHERE name = 'speedy'")
        status = database.cursor.fetchone()
        self.assertEqual('Not taking orders.', status[0])

    def test_is_there_such_restaurant(self):
        database.create_menu_table('speedy')
        self.assertTrue(database.is_there_such_restaurant('speedy'))

    def test_is_there_not_existing_restaurant(self):
        self.assertFalse(database.is_there_such_restaurant('speedy'))

    def test_is_open_closed(self):
        database.create_menu_table('speedy')
        self.assertFalse(database.is_open('speedy'))

    def test_is_open_opened(self):
        database.create_menu_table('speedy')
        database.open('speedy')
        self.assertTrue(database.is_open('speedy'))

    def test_valid_product(self):
        database.create_menu_table('speedy')
        database.add('speedy', 'pizza', 3.5)
        self.assertTrue(database.valid_product('speedy', 'pizza'))

    def test_not_valid_product(self):
        database.create_menu_table('speedy')
        database.add('speedy', 'pizza', 3.5)
        self.assertFalse(database.valid_product('speedy', 'spaghetti'))

    def test_status_of_an_order(self):
        database.ready('Barney', [('pizza', 3.5), ('coke', 2.5)])
        self.assertEqual("Status of your order is Preparing.",
                         database.status_orders('Barney'))

    def test_status_of_an_not_existing_order(self):
        self.assertEqual("You have no orders",
                         database.status_orders('Barney'))

    def test_delivery_tax_existing_district(self):
        database.add_district('Lulin', 4)
        self.assertEqual((True, 4), database.delivery_tax('Lulin'))

    def test_delivery_tax_unexisting_district(self):
        self.assertEqual((False, 0), database.delivery_tax('Lulin'))

    def test_status_unexisting_restaurant(self):
        self.assertEqual("There is no such restaurant",
                         database.status_restaurant('speedy'))

    def test_status_existing_restaurant(self):
        database.create_menu_table('speedy')
        self.assertEqual("Status is Not busy",
                         database.status_restaurant('speedy'))

    def tearDown(self):
        database.cursor.execute('DROP TABLE users')
        database.cursor.execute('DROP TABLE restaurants')
        database.cursor.execute('DROP table orders')
        database.cursor.execute('DROP table taxes')


if __name__ == '__main__':
    unittest.main()
