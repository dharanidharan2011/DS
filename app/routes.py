from flask import Blueprint, render_template

main = Blueprint("main", __name__)

# Sample 5 products
products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 1999,
        "image": "https://via.placeholder.com/150"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 2999,
        "image": "https://via.placeholder.com/150"
    },
    {
        "id": 3,
        "name": "Bluetooth Speaker",
        "price": 1499,
        "image": "https://via.placeholder.com/150"
    },
    {
        "id": 4,
        "name": "Gaming Mouse",
        "price": 999,
        "image": "https://via.placeholder.com/150"
    },
    {
        "id": 5,
        "name": "Mechanical Keyboard",
        "price": 2499,
        "image": "https://via.placeholder.com/150"
    }
]

@main.route("/")
def home():
    return render_template("index.html", products=products)
