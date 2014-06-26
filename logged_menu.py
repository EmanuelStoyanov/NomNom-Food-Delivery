import database


def logged_menu(valid_user):
    print("Welcome.You are logged in as " + valid_user.username)

    while True:
        command = input("(%s)Enter command or 'help' to see all commands>" % valid_user.username)

        if command == 'help':
            help()

        elif command == 'order':
            order()

        elif command == 'exit':
            break


def help():
    print("command 'order' - if you want to see the menu and order")
    print("command 'delivery tax' - if you want to see \
    what is the delivery tax")
    print("command 'cart' - if you want to see your cart")
    print("command 'status' - if you want to see status of the orders")
    print("command 'exit' - if you want to exit to normal mode")


def order():
    print("These are our restaurants")
    database.display_restaurants()
    restaurant = input("Which menu you want to see: ")
    database.menu(restaurant)

    if database.is_open(restaurant):
        print("This restaurant is currently open!")
        command = input("If you want to add something to the cart type 'add'>")
        if command == 'add':
            print("Adding")
    else:
        print("This restaurant is currently not open, sorry")

