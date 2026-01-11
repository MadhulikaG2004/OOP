from product import Product
class productCatalog:
    def __init__(self):
        self.products=[]
    def add_product(self,product:Product):
        self.products.append(product)
    def view_product(self):
        for p in self.products:
            print("Name is",p.name)
            print(p.price)
            print(p.stock_quantity)
    def getproduct(self,product_name):
        for p in self.products:
            if p.name==product_name:
                return p
    
    