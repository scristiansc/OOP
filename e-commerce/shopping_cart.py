
class ShoppingCart:
    def __init__(self):
        self.products = []


    def add_item(self, product):
        if product not in self.products:
            self.products.append(product)
        else:
            print("The product is already in the cart")


    def remove_item(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("The product is not in the cart")


    def get_items(self):
        return self.products


    def get_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
