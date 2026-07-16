from app import app

client = app.test_client()


# Testing the home route.
def test_home():
    response = client.get("/")
    assert response.status_code == 200


# Testing to getting all inventory items.
def test_get_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200


# Testing to getting one inventory item.
def test_get_inventory_item():
    response = client.get("/inventory/1")
    assert response.status_code == 200


# Test adding a new inventory item.
def test_add_inventory_item():

    new_item = {
        "name": "Milk",
        "brand": "Brookside",
        "price": 250,
        "stock": 10
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code == 201


# Test updating an inventory item.
def test_update_inventory_item():

    response = client.patch(
        "/inventory/1",
        json={
            "price": 400,
            "stock": 30
        }
    )

    assert response.status_code == 200


# Test deleting an inventory item.
def test_delete_inventory_item():

    response = client.delete("/inventory/2")

    assert response.status_code == 200

# Test searching the OpenFoodFacts API.
def test_search_product(): 
    response = client.get("/search/737628064502") 
    assert response.status_code == 200