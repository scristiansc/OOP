
class ShoppingCart:
    def __init__(self):
        self.__products = []


    def add_item(self, product):
        if product not in self.__products:
            self.__products.append(product)
        else:
            print("The product is already in the cart")


    def remove_item(self, product):
        if product in self.__products:
            self.__products.remove(product)
        else:
            print("The product is not in the cart")


    def get_items(self):
        return self.__products


    def get_total(self):
        total = 0
        for product in self.__products:
            total += product.price
        return total
