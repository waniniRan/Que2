import requests

BASE_URL = "http://127.0.0.1:5000/products"

def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def list_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

# Example usage
add_product("Laptop", "A high-performance laptop", 999.99)
add_product("Smartphone", "A powerful smartphone", 499.99)
list_products()