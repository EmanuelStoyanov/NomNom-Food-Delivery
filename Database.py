import sqlite3
from User import User

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
    if username == 'admin':
        return False
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
    user = cursor.fetchone()

    if(user):
        return User(user[0], user[2])

    return False


def admin(password):
    query = "SELECT password FROM users WHERE username = ?"

    cursor.execute(query, ('admin', ))
    admin_pass = cursor.fetchone()

    if password == admin_pass[0]:
        return True

    return False
