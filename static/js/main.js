// ---------------------------
// SIMPLE CART FUNCTIONALITY
// ---------------------------

let cart = [];

// Add product to cart
function addToCart(id, name, price) {
    // Check if product already in cart
    let existing = cart.find(item => item.id === id);
    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({ id: id, name: name, price: price, quantity: 1 });
    }
    alert(name + " added to cart!");
    updateCartUI();
}

// Update cart in UI (optional display)
function updateCartUI() {
    const cartCount = document.getElementById("cart-count");
    if(cartCount) {
        let totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCount.innerText = totalItems;
    }
}

// Simple DOMContentLoaded event
document.addEventListener("DOMContentLoaded", () => {
    // Attach add to cart buttons
    const buttons = document.querySelectorAll(".product-card button");
    buttons.forEach((btn, index) => {
        btn.addEventListener("click", () => {
            // Assuming products array in JS (or pass from Flask if needed)
            let product = window.products[index]; // you can inject products array from Flask
            addToCart(product.id, product.name, product.price);
        });
    });
});
