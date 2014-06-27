import database


def logged_menu(valid_user):
    print("Welcome.You are logged in as " + valid_user.get_username())

    while True:
        command = input("(%s)Enter command or 'help' "
                        "to see all commands>" % valid_user.get_username())

        if command == 'help':
            help()

        elif command == 'order':
            order(valid_user)

        elif command == 'cart':
            cart(valid_user)

        elif command == 'status orders':
            status_orders(valid_user)

        elif command == 'status restaurant':
            status_restaurant()

        elif command == 'delivery tax':
            delivery_tax()

        elif command == 'exit':
            break

        else:
            print("Wrong command!")


def help():
    print("command 'order' - if you want to see the menu and order")
    print("command 'delivery tax' - if you want to see "
          "what is the delivery tax")
    print("command 'cart' - if you want to see your cart")
    print("command 'status orders' - if you want to see status of the orders")
    print("command 'status restaurant' - "
          "if you want to see status of the restaurant")
    print("command 'exit' - if you want to exit to normal mode")


def order(valid_user):
    print("These are our restaurants")
    database.display_restaurants()
    restaurant = input("Which menu you want to see: ")

    if database.is_there_such_restaurant(restaurant):
        database.menu(restaurant)
    else:
        print("There is no such restaurant")
        return False

    if database.is_open(restaurant):
        print("This restaurant is currently open!")

        while True:

            command = input("Type 'add','remove','ready' or 'exit'>")

            if command == 'add':
                add(valid_user, restaurant)

            elif command == 'remove':
                remove(valid_user)

            elif command == 'ready':
                final_details(valid_user)
                break

            elif command == 'exit':
                break

            else:
                print("Wrong command!")

    else:
        print("This restaurant is currently not open, sorry")


def cart(valid_user):
    sum = 0
    print("You have in cart:")
    if valid_user.get_basket():
        for product_price in valid_user.get_basket():
            sum += product_price[1]
            print(product_price[0] + " - " + str(product_price[1]))
        print("Total sum without delivery:" + str(sum))
    else:
        print("You have nothing in cart yet")


def final_details(valid_user):
    print("This is the final step.")
    cart(valid_user)

    command = input("Are you sure that's all? y/n? ")
    if command == 'y':

        if not delivery_tax():
            return False

        command2 = \
            input("Is this where you want to receive the order: "
                  + valid_user.get_address() + " y/n?")

        if command2 == 'y':
            database.ready(valid_user.get_username(), valid_user.get_basket())
            print("Order is taken.")
        elif command2 == 'n':
            new_address = input("Where to send the order: ")
            valid_user.set_address(new_address)
            database.ready(valid_user.get_username(), valid_user.get_basket())
            print("Order is taken and will be sent to the new address")
        else:
            print("Wrong command")

    valid_user.set_basket([])


def status_orders(valid_user):
    print(database.status_orders(valid_user))


def delivery_tax():
    district = input("Please type your district to calculate delivery tax: ")
    tax = database.delivery_tax(district)
    if not tax[0]:
        print("Sorry, we do not send to this district")
        return False
    else:
        print("Your delivery tax will be " + str(tax[1]))
        return True


def add(valid_user, restaurant):
    product = input("Which product do you want to add? ")
    product_price = database.valid_product(restaurant, product)
    if product_price:
        valid_user.get_basket().append(product_price)
        cart(valid_user)
    else:
        print("This product is not on the menu")


def remove(valid_user):
    removed = input("Which item do you want to remove? ")
    for product_price in valid_user.get_basket():
        if removed == product_price[0]:
            valid_user.get_basket().remove(product_price)
            return True

    print("There is no such thing in basket")
    return False


def status_restaurant():
    restaurant = input("Which restaurant's status you want to check? ")
    print(database.status_restaurant(restaurant))
