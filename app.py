from flask import Flask, jsonify, request
# request lets us receive JSON data sent by the client.
app = Flask(__name__)

# Simulated inventory database
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Almond",
        "price": 350,
        "stock": 20
    },
    {
        "id": 2,
        "name": "Peanut Butter",
        "brand": "Nutty",
        "price": 500,
        "stock": 15
    }
]

# This is the Home route.
# It displays a welcome message.
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Inventory Management API"})


# This route returns all inventory items.
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

# This route returns one inventory item by its ID.
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):

    # this Loops through the inventory list.
    for item in inventory:

        # Check if the ID matches.
        if item["id"] == item_id:
            return jsonify(item), 200

    # this rreturns an error if the item does not exist.
    return jsonify({"error": "Item not found"}), 404

# This route adds a new inventory item.
@app.route("/inventory", methods=["POST"])
def add_inventory_item():

    # Get the JSON data from the request.
    data = request.get_json()

    # Check that all required fields are provided.
    required_fields = ["name", "brand", "price", "stock"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Create a new ID.
    new_id = len(inventory) + 1

    # Create the new inventory item.
    new_item = {
        "id": new_id,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"]
    }

    # Add it to the inventory list.
    inventory.append(new_item)

    # Return the new item.
    return jsonify(new_item), 201


if __name__ == "__main__":
    app.run(debug=True)