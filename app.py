from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(debug=True)