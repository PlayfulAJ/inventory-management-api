import requests

BASE_URL = "http://127.0.0.1:5000"


# this Displays all the menu options.
def menu():
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Search Product")
    print("3. Exit")


while True:

    menu()

    choice = input("Choose an option: ")

    # this Views all inventory items.
    if choice == "1":

        response = requests.get(f"{BASE_URL}/inventory")

        print(response.json())

    # Search a product using its barcode.
    elif choice == "2":

        barcode = input("Enter product barcode: ")

        response = requests.get(f"{BASE_URL}/search/{barcode}")

        print(response.json())

    # To Exit the program.
    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")