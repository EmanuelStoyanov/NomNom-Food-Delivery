import database


def logged_menu(valid_user):
    print("Welcome.You are logged in as " + valid_user.username)

    while True:
        command = input("(%s)Enter command or 'help' to see all commands>" % valid_user.username)

        if command == 'help':
            help()

        elif command == 'order':
            order(valid_user)

        elif command == 'exit':
            break


def help():
    print("command 'order' - if you want to see the menu and order")
    print("command 'delivery tax' - if you want to see \
    what is the delivery tax")
    print("command 'cart' - if you want to see your cart")
    print("command 'status' - if you want to see status of the orders")
    print("command 'exit' - if you want to exit to normal mode")


def order(valid_user):
    print("These are our restaurants")
    database.display_restaurants()
    restaurant = input("Which menu you want to see: ")
    database.menu(restaurant)

    if database.is_open(restaurant):
        print("This restaurant is currently open!")

    while True:

        command = input("Type 'add' or 'exit'>")
        if command == 'add':
            product = input("Which product do you want to add? ")
            product_price = database.valid_product(restaurant, product)
            if product_price:
                valid_user.basket.append(product_price)
                print(valid_user.basket)
            else:
                print("This product is not on the menu")

        elif command == 'exit':
            break

        else:
            print("Wrong command!")
    else:
        print("This restaurant is currently not open, sorry")

