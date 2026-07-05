from flask import Flask, jsonify

app = Flask(__name__)

# This is the  Home route
# it displays a welcome message.
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Inventory Management API"})


if __name__ == "__main__":
    app.run(debug=True)