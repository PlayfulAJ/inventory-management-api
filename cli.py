import requests

BASE_URL = "http://127.0.0.1:5000"


# This Displays all the menu options.
def menu():
    print("\nInventory Management System")
    print("1. View All Inventory")
    print("2. View One Inventory Item")
    print("3. Add Inventory Item")
    print("4. Update Inventory Item")
    print("5. Delete Inventory Item")
    print("6. Search Product")
    print("7. Exit")


while True:

    menu()

    choice = input("Choose an option: ")

    # View all inventory items.
    if choice == "1":

        response = requests.get(f"{BASE_URL}/inventory")

        print(response.json())

    # View one inventory item.
    elif choice == "2":

        item_id = input("Enter item ID: ")

        response = requests.get(f"{BASE_URL}/inventory/{item_id}")

        print(response.json())

    # Add a new inventory item.
    elif choice == "3":

        name = input("Enter product name: ")
        brand = input("Enter brand: ")
        price = int(input("Enter price: "))
        stock = int(input("Enter stock: "))

        new_item = {
            "name": name,
            "brand": brand,
            "price": price,
            "stock": stock
        }

        response = requests.post(
            f"{BASE_URL}/inventory",
            json=new_item
        )

        print(response.json())

    # Update an inventory item.
    elif choice == "4":

        item_id = input("Enter item ID: ")

        price = int(input("Enter new price: "))
        stock = int(input("Enter new stock: "))

        updated_item = {
            "price": price,
            "stock": stock
        }

        response = requests.patch(
            f"{BASE_URL}/inventory/{item_id}",
            json=updated_item
        )

        print(response.json())

    # Delete an inventory item.
    elif choice == "5":

        item_id = input("Enter item ID: ")

        response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

        print(response.json())

    # Search for a product using its barcode.
    elif choice == "6":

        barcode = input("Enter product barcode: ")

        response = requests.get(f"{BASE_URL}/search/{barcode}")

        print(response.json())

    # Exit the program.
    elif choice == "7":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")