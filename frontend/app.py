import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://product-service:5001"
)

@app.route("/")
def home():
    products = []
    error = None

    try:
        response = requests.get(
            f"{PRODUCT_SERVICE_URL}/products",
            timeout=5
        )
        response.raise_for_status()
        products = response.json()
    except requests.RequestException:
        error = "Unable to load products. Please try again."

    return render_template(
        "index.html",
        products=products,
        error=error
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)