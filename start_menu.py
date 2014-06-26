import database
from admin_menu import admin_menu
from logged_menu import logged_menu


def start_menu():
    print("Hello and welcome to NomNom Food Delivery!!")
    print("If you want to order please register or login")

    while True:
        command = input("Enter command or 'help' to see all commands>")

        if command == 'help':
            help()

        elif command == 'exit':
            break

        elif command == 'register':
            register()

        elif command == 'login':
            login()

        elif command == 'admin':
            admin()

        else:
            print("You have entered an invalid command")


def help():
    print("command 'login' - if you already have an account")
    print("command 'register' - if you want to create new account")
    print("command 'exit' - if you want to close the program")
    print("command 'admin' - if you have admin rights")


def register():
    username = input("Username: ")
    password = input("Password: ")
    address = input("Address(Don't worry, you could change it later):")

    is_registered = database.register(username, password, address)
    if is_registered:
        print("Registration Successful")
    else:
        print("That username has already been taken")


def login():
    username = input("Valid username: ")
    password = input("Valid password: ")

    valid_user = database.login(username, password)

    if valid_user:
        logged_menu(valid_user)
    else:
        print("Invalid username or password, please try again")


def admin():
    print("You are trying to access admin account")
    admin_password = input('Admin password:')

    is_admin = database.admin(admin_password)

    if is_admin:
        admin_menu()
    else:
        print("Sorry, wrong admin password")


def main():
    database.create_users_table()
    database.create_restaurant_table()
    start_menu()

if __name__ == '__main__':
    main()

