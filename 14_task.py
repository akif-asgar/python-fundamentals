products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Phone", "price": 800, "stock": 10},
    {"name": "Headphones", "price": 150, "stock": 20}
]

cart = []

while True:

    input_product = input("Enter product name (or 'q' to quit, 'cart' to view): ")

    if input_product.lower() == 'q':
        print("Exiting the store. Thank you!")
        break

    elif input_product.lower() == 'cart':

        total = sum(item["price"] * item["qty"] for item in cart)

        print("Your cart:")
        for item in cart:
            print(f"{item['name']} x{item['qty']} - ${item['price']} each")

        print(f"Total: ${total}")

        pay = input("Enter money to pay or 'c' to cancel: ")

        if pay.lower() == 'c':
            print("Payment cancelled.")

        elif pay.isdigit() and int(pay) >= total:
            change = int(pay) - total
            print(f"Payment successful! Change: ${change}")

            cart.clear()

        else:
            print("Not enough money!")

    else:

        product = next((p for p in products if p["name"].lower() == input_product.lower()), None)

        if product:

            if product["stock"] > 0:

                
                item_in_cart = next((i for i in cart if i["name"] == product["name"]), None)

                if item_in_cart:
                    item_in_cart["qty"] += 1
                else:
                    cart.append({
                        "name": product["name"],
                        "price": product["price"],
                        "qty": 1
                    })

                product["stock"] -= 1

                print(f"Added {product['name']} to cart.")

            else:
                print("Out of stock!")

        else:
            print("Product not found.")