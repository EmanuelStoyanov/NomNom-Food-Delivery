import sqlite3
from user import user

conn = sqlite3.connect("Users.db")
cursor = conn.cursor()


def create_users_table():
    create_query = '''create table if not exists
                      users(
                      username TEXT,
                      password TEXT,
                      address TEXT)'''

    cursor.execute(create_query)

    admin_query = "SELECT username FROM users where username = 'admin' "
    cursor.execute(admin_query)
    admin = cursor.fetchone()

    if not admin:
        register_admin = "INSERT INTO users (username, password) \
        values (?, ?)"
        cursor.execute(register_admin, ('admin', 'ADMINNOMNOM'))

    conn.commit()


def register(username, password, address):
    select_query = "SELECT username FROM users"
    usernames = cursor.execute(select_query)
    for row in usernames:
        if username == row[0]:
            return False
    conn.commit()

    insert = "insert into users (username, password, address) values (?, ?, ?)"
    cursor.execute(insert, (username, password, address))
    conn.commit()
    return True


def login(username, password):
    if username == 'admin':
        return False

    select_query = "SELECT username, password, address FROM users \
    WHERE username = ? AND password = ? LIMIT 1"

    cursor.execute(select_query, (username, password))
    current_user = cursor.fetchone()

    if(current_user):
        return user(current_user[0], current_user[2])

    return False


def admin(password):
    query = "SELECT password FROM users WHERE username = ?"

    cursor.execute(query, ('admin', ))
    admin_pass = cursor.fetchone()

    if password == admin_pass[0]:
        return True

    return False


def create_restaurant_table():
    create_query = '''create table if not exists
                    restaurants(
                    name TEXT,
                    is_open INTEGER,
                    status TEXT)'''
    cursor.execute(create_query)
    conn.commit()


def create_orders_table():
    create_query = '''create table if not exists
                    orders(
                    username TEXT,
                    product TEXT,
                    price REAL,
                    status TEXT)'''
    cursor.execute(create_query)
    conn.commit()


def create_taxes_table():
    create_query = '''create table if not exists
                    taxes(
                    district TEXT,
                    tax REAL)'''
    cursor.execute(create_query)
    conn.commit()


def create_menu_table(new_restaurant):
    create_query = "create table if not exists %s \
    (products TEXT,price REAL)" % new_restaurant

    cursor.execute(create_query)

    existance_query = "SELECT name FROM restaurants"
    names = cursor.execute(existance_query)
    for row in names:
        if new_restaurant == row[0]:
            print("This restaurant already exists.")
            return False

    status = "INSERT INTO restaurants (name, is_open, status) \
    values (?, ?, ?)"
    cursor.execute(status, (new_restaurant, 0, 'Not busy'))

    conn.commit()
    return True


def is_there_such_restaurant(restaurant):
    is_there_query = "SELECT name FROM restaurants WHERE name = ?"
    cursor.execute(is_there_query, (restaurant, ))
    restaurant = cursor.fetchone()

    if not restaurant:
        return False

    return True


def add(restaurant, product, price):
    select_query = "SELECT products FROM %s" % restaurant
    products = cursor.execute(select_query)

    for row in products:
        if product == row[0]:
            print("This product is already in the catalog")
            return False

    add_query = "INSERT INTO %s (products, price) \
    values (?, ?)" % restaurant
    cursor.execute(add_query, (product, price))

    conn.commit()
    return True


def open(restaurant):
    status_query = "SELECT is_open FROM restaurants WHERE name = ?"
    cursor.execute(status_query, (restaurant, ))
    status = cursor.fetchone()

    if status[0]:
        print("It is already open.")
        return False
    else:
        open_query = "UPDATE restaurants SET is_open = 1 WHERE name = ?"
        cursor.execute(open_query, (restaurant, ))

    conn.commit()
    return True


def close(restaurant):
    status_query = "SELECT is_open FROM restaurants WHERE name = ?"
    cursor.execute(status_query, (restaurant, ))
    status = cursor.fetchone()

    if status[0] == 0:
        print("It is already closed.")
        return False
    else:
        close_query = "UPDATE restaurants SET is_open = 0 WHERE name = ?"
        cursor.execute(close_query, (restaurant, ))

    conn.commit()
    return True


def update_status_restaurant(restaurant, new_status):
    status_query = "UPDATE restaurants SET status = ? \
    WHERE name = ?"
    cursor.execute(status_query, (new_status, restaurant))
    conn.commit()


def status_delivery(username, new_status):
    status_query = "UPDATE orders SET status = ? \
    WHERE username = ?"
    cursor.execute(status_query, (new_status, username))
    conn.commit()


def display_restaurants():
    display_query = "SELECT name FROM restaurants"
    restaurants = cursor.execute(display_query)

    for row in restaurants:
        print(row[0])


def menu(restaurant):
    display_query = "SELECT products,price FROM %s" % restaurant
    cursor.execute(display_query)
    products = cursor.fetchall()

    print("product - price")
    for row in products:
        print(row[0] + " - " + str(row[1]))


def is_open(restaurant):
    open_query = "SELECT is_open FROM restaurants WHERE name = ?"
    cursor.execute(open_query, (restaurant, ))
    status = cursor.fetchone()

    return status[0]


def valid_product(restaurant, product):
    select_query = "SELECT products, price \
    FROM %s WHERE products = ?" % restaurant
    cursor.execute(select_query, (product, ))
    product_price = cursor.fetchone()

    return product_price


def ready(username, basket):
    for product in basket:
        add_query = "INSERT INTO orders \
        (username, product, price, status) values (?, ?, ?, ?)"
        cursor.execute(add_query,
                      (username, product[0], product[1], "Preparing."))
    conn.commit()


def status_orders(valid_user):
    show_status = "SELECT status FROM orders WHERE username = ? LIMIT 1"
    cursor.execute(show_status, (valid_user.get_username(), ))
    status = cursor.fetchone()

    if status:
        return "Status of your order is " + status[0]
    else:
        return "You have no orders"


def add_district(district, tax):
    add_district = "INSERT INTO taxes (district, tax) values (?, ?)"
    cursor.execute(add_district, (district, tax))
    conn.commit()


def delivery_tax(district):
    tax_query = "SELECT tax FROM taxes WHERE district = ?"
    cursor.execute(tax_query, (district, ))
    tax = cursor.fetchone()

    if not tax:
        return (False, 0)

    return (True, tax[0])


def status_restaurant(restaurant):
    status_query = "SELECT status FROM restaurants WHERE name = ?"
    cursor.execute(status_query, (restaurant, ))
    status = cursor.fetchone()

    if not status:
        return "There is no such restaurant"
    else:
        return "Status is " + status[0]
