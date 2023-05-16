Menu = {
    'coffee':12 ,
    'tea':10 ,
    'chicken fillet':35,
    'cheeseburger':30,
}
cost = 0

def display_menu():
    print("Welcome to the ITI Cafe!")
    print("1. View Menu")
    print("2. Place Order")
    print("3. Exit")

def admin_login():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    # Perform authentication logic here
    if admin_username == "admin" and admin_password == "admin@password":
        return True
    else:
        print("Invalid admin credentials.")
        return False

def view_menu():
    print("Menu: ", Menu)
    

def place_order():
    order = input("Enter your order : ")
    quantity = input ("Enter quantity : ")
    cost = cost + int(Menu[order])*int(quantity)
    # Process the order and calculate the total cost
    print ("You Ordered ", order , " ",quantity,"X\nTotal Cost = ",cost)

def cafeteria():
    while True:
        display_menu()
        option = input("Enter your choice: ")
        if option == "1":
            view_menu()
        elif option == "2":
            place_order()
        elif option == "3":
            print("Thank you for visiting. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_panel():
    while True:
        print("Admin Panel:")
        print("1. Login")
        print("2. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            if admin_login():
                # Perform admin operations here
                print("You are now logged in as an admin.")
                choice = input ("1. Add Items To Menu\n2. Update Menu\n3. Remove Item\nEnter your choice: ")
                if choice == '1':
                    new_item=input("Enter New Item ")
                    price = input("Enter Price ")
                    Menu.update({new_item:price})
                elif choice == '2':
                    item_update = input("Enter Item To Be Updated ")
                    price_update = input("Enter New Price Update ")
                    Menu[item_update]=price_update
                elif choice == '3':
                    item_delete = input("Enter Item To Be Deleted ")
                    Menu.pop[item_delete]
                break
        elif option == "2":
            print("Exiting admin panel.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Cafeteria ITI!")
    while True:
        print("Select user type:")
        print("1. Client")
        print("2. Admin")
        print("3. Exit")
        user_type = input("Enter your choice: ")
        if user_type == "1":
            cafeteria()
        elif user_type == "2":
            admin_panel()
        elif user_type == "3":
            print("Exiting the Cafeteria System.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
