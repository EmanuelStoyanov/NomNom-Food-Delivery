import database


def admin_menu():
    print("Welcome.You are logged as admin.")

    while True:
        command = input("(admin)Enter command or 'help' to see all commands>")

        if command == 'help':
            help()

        elif command == 'new':
            new()

        elif command == 'switch':
            break


def help():
    print("command 'new' - if you want to add new restaurant")
    print("command 'change' - if you want to change the menu")
    print("command 'switch' - if you want to switch to normal mode")
    print("command 'open' - if you want to open a restaurant")
    print("command 'close' - if you want to close a restaurant")
    print("command 'status' - if you want to change restaurant's status")


def new():
    new_restaurant = input("Enter the name of the new restaurant: ")
    database.create_restaurant_table(new_restaurant)
