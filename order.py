from enum import Enum
from payment_gateway import PaymentGateway
from product_catalog import productCatalog
class OrderStatus(Enum):
    CREATED="CREATED"
    PAID="PAID"
    CANCELLED="CANCELLED"

class order:
    def __init__(self,order_id,product_item,user,payment_gateway:PaymentGateway):
        self.order_id=order_id
        self.product_item=product_item
        self.user=user
        self.payment_gateway=payment_gateway
        self.order_status=OrderStatus.CREATED
    def place_order(self):
        total_amount=self.calculate_total()
        self.payment_gateway.initiate_payment(total_amount)
        user1=self.user
        print(user1.order_history)
        user1.set_order_history("order 1")
        print(user1.order_history)
        print("Thank you payment completed!")
    def cancel_order(self,id):
        orders=self.user.order_history
        for o in orders:
            if o.order_id==id:
                o.order_status=OrderStatus.CANCELLED
    def calculate_total(self):
        cart=self.product_item
        amount=0
        for c in cart:
            amount=amount+(c["product"].price)*c["quantity"]
        return amount