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

        elif command == 'exit':
            break

        elif command == 'register':
            username = input("Username: ")
            password = input("Password: ")

            Database.register(username, password)
            print("Registration Successful")

        elif command == 'login':
            username = input("Valid username: ")
            password = input("Valid password: ")

            valid_user = Database.login(username, password)

            if valid_user:
                print("You are logged in")
            else:
                print("Invalid username or password, please try again")

        else:
            print("You have entered an invalid command")


def main():
    Database.create_users_table()
    start_menu()

if __name__ == '__main__':
    main()

