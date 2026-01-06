class User:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.order_history=[]
    def set_order_history(self,order):
        self.order_history.append(order)
    def view_order_history(self):
        print("Order History")
        print(self.order_history)
        