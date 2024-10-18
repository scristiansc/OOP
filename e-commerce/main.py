
from shopping_cart import ShoppingCart
from product import Product

#Create some products
iphone = Product("Iphone 15 pro", 2_000)
pixel = Product("Pixel 9pro", 2_100)
samsung = Product("Galaxy s22", 3_000)

#Create a shopping cart
cart = ShoppingCart()

#Add products to the cart
cart.add_item(iphone)
cart.add_item(pixel)
cart.add_item(samsung)
cart.add_item(iphone) #Trying to add a duplicate product

# Remove a product from the cart
cart.remove_item(pixel)

# Get the products in the cart
print("Products in the cart: ")
for product in cart.get_items():
    print(f"-{product.name}:  ${product.price}")

# Get the cart total
print(f"Cart total: ${cart.get_total()}")