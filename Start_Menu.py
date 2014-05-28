import Database


def start_menu():
    print("Hello and welcome to NomNom Food Delivery!!")
    print("If you want to order please register or login")

    while True:
        command = input("Enter command or 'help' to see all commands>")

        if command == 'help':
            print("command 'login' - if you already have an account")
            print("command 'register' - if you want to create new account")
            print("command 'exit' - if you want to close the program")
            print("command 'admin' - if you have admin rights")

        elif command == 'exit':
            break

        elif command == 'register':
            username = input("Username: ")
            password = input("Password: ")
            address = input("Address(Don't worry, you could change it later):")

            is_registered = Database.register(username, password, address)
            if is_registered:
                print("Registration Successful")
            else:
                print("You cannot register username 'admin'")

        elif command == 'login':
            username = input("Valid username: ")
            password = input("Valid password: ")

            valid_user = Database.login(username, password)

            if valid_user:
                print("You are logged in")
            else:
                print("Invalid username or password, please try again")

        elif command == 'admin':
            print("You are trying to access admin account")
            admin_password = input('Admin password:')

            is_admin = Database.admin(admin_password)

            if is_admin:
                print("Okay you're in.Now you can modify the menu")
            else:
                print("Sorry, wrong admin password")

        else:
            print("You have entered an invalid command")


def main():
    Database.create_users_table()
    start_menu()

if __name__ == '__main__':
    main()

