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


def create_restaurant_table(new_restaurant):
    create_query = "create table if not exists %s \
    (is_open INTEGER,status TEXT,products TEXT,price REAL)" % new_restaurant

    cursor.execute(create_query)

    status = "INSERT INTO %s (is_open, status) \
    values (?, ?)" % new_restaurant
    cursor.execute(status, (1, 'Not busy'))
    conn.commit()
