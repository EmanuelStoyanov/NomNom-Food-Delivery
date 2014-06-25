import database


def admin_menu():
    print("Welcome.You are logged as admin.")

    while True:
        command = input("(admin)Enter command or 'help' to see all commands>")

        if command == 'help':
            help()

        elif command == 'new':
            new()

        elif command == 'add':
            add()

        elif command == 'open':
            open()

        elif command == 'close':
            close()

        elif command == 'exit':
            break


def help():
    print("command 'new' - if you want to add new restaurant")
    print("command 'add' - if you want to add the menu")
    print("command 'open' - if you want to open a restaurant")
    print("command 'close' - if you want to close a restaurant")
    print("command 'status' - if you want to change restaurant's status")
    print("command 'exit' - if you want to exit to normal mode")


def new():
    new_restaurant = input("Enter the name of the new restaurant: ")
    database.create_restaurant_table(new_restaurant)


def add():
    restaurant = input("Name of the restaurant: ")
    product = input("What do you want to add to the menu: ")
    price = input("What is the price of this product :")
    database.add(restaurant, product, price)


def open():
    restaurant = input("Which restaurant you want to open: ")
    database.open(restaurant)


def close():
    restaurant = input("Which restaurant you want to close: ")
    database.close(restaurant)
