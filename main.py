products = {
    "olma": 5000,
    "banan": 7000,
    "non": 3000
}

cart = {}

def add_to_cart(product, qty):
    if product in products:
        cart[product] = cart.get(product, 0) + qty
    else:
        print("❌ Mahsulot yo‘q")

def total_price():
    return sum(products[p] * q for p, q in cart.items())

add_to_cart("olma", 2)
add_to_cart("non", 1)
print("🛒 Jami:", total_price(), "so‘m")
