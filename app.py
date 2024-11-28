from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity (can be replaced with a database)
products = []

# validate product data
def validate_product(data):
    if not all(key in data for key in ["name", "description", "price"]):
        return "Missing fields"
    if not isinstance(data["price"], (int, float)):
        return "Invalid price format"
    return None

# API endpoint to create a new product

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    error = validate_product(data)
    if error:
        return jsonify({"error": error}), 400
    
    product = {
        "id": len(products) + 1,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"]
    }
    products.append(product)
    return jsonify(product), 201

# API endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
