class Product:
    def __init__(self,name,category,stock_quantity,price):
        self.name=name
        self.category=category
        self.stock_quantity=stock_quantity
        self.price=price

    def is_available(self,quantity):
           
            if self.stock_quantity>=quantity:
                    return True
            return False

        