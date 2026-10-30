from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mobile Phone", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2500}
]

@app.route("/")
def home():
    return jsonify({
        "service": "product-service",
        "status": "running"
    })

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)