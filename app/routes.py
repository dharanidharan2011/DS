from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)

# Sample products
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

# Home page
@main.route("/")
def home():
    return render_template("index.html", products=products)

# Products page
@main.route("/products")
def show_products():
    return render_template("products.html", products=products)

# Login page
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # handle login logic here
        return redirect(url_for("main.home"))
    return render_template("login.html")

# Register page
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # handle registration logic here
        return redirect(url_for("main.login"))
    return render_template("register.html")

# Cart page
@main.route("/cart")
def cart():
    return render_template("cart.html")

# Checkout page
@main.route("/checkout")
def checkout():
    return render_template("checkout.html")

# Admin page
@main.route("/admin")
def admin():
    return render_template("admin.html")
