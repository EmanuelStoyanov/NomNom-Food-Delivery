import database


def logged_menu(valid_user):
    print("Welcome.You are logged in as " + valid_user.username)

    while True:
        command = input("(%s)Enter command or 'help' to see all commands>" % valid_user.username)

        if command == 'help':
            help()

        elif command == 'menu':
            menu()

        elif command == 'exit':
            break


def help():
    print("command 'menu' - if you want to see the whole menu")
    print("command 'delivery tax' - if you want to see \
    what is the delivery tax")
    print("command 'cart' - if you want to see your cart")
    print("command 'status' - if you want to see status of the orders")
    print("command 'exit' - if you want to exit to normal mode")


def menu():
    print("These are our restaurants")
    database.display_restaurants()
    restaurants = input("Which menu you want to see: ")
    database.menu(restaurants)
