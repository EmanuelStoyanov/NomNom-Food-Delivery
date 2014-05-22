import sqlite3
from User import User

conn = sqlite3.connect("Users.db")
cursor = conn.cursor()


def create_users_table():
    create_query = '''create table if not exists
                      users(
                      username TEXT,
                      password TEXT)'''

    cursor.execute(create_query)


def register(username, password):
    insert = "insert into users (username, password) values (?, ?)"
    cursor.execute(insert, (username, password))
    conn.commit()


def login(username, password):
    select_query = "SELECT username, password FROM users \
    WHERE username = ? AND password = ? LIMIT 1"

    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return User(user[0])
    else:
        return False
