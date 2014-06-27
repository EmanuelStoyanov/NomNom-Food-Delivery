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

        elif command == 'status restaurant':
            update_status_restaurant()

        elif command == 'status delivery':
            status_delivery()

        elif command == 'add district':
            add_district()

        elif command == 'exit':
            break

        else:
            print("You have entered an invalid command")


def help():
    print("command 'new' - if you want to add new restaurant")
    print("command 'add' - if you want to add the menu")
    print("command 'open' - if you want to open a restaurant")
    print("command 'close' - if you want to close a restaurant")
    print("command 'status restaurant' - if you want to change restaurant's status")
    print("command 'status delivery' - if you want to change delivery's status")
    print("command 'exit' - if you want to exit to normal mode")


def new():
    new_restaurant = input("Enter the name of the new restaurant: ")
    database.create_menu_table(new_restaurant)


def add():
    restaurant = input("Name of the restaurant: ")
    if database.is_there_such_restaurant(restaurant):
        product = input("What do you want to add to the menu: ")
        price = input("What is the price of this product :")
        database.add(restaurant, product, price)
    else:
        print("There is no such restaurant")


def open():
    restaurant = input("Which restaurant you want to open: ")
    database.open(restaurant)


def close():
    restaurant = input("Which restaurant you want to close: ")
    database.close(restaurant)


def update_status_restaurant():
    restaurant = input("Which restaurant's status you want to change: ")
    new_status = input("What should be the new status? ")
    database.update_status_restaurant(restaurant, new_status)


def status_delivery():
    username = input("Which username's delivery status you want to change: ")
    new_status = input("What should be the new status? ")
    database.status_delivery(username, new_status)


def add_district():
    district = input("Which district you want to add: ")
    tax = input("What should be the delivery tax? ")
    database.add_district(district, tax)
