from User import User
from product import Product
from product_catalog import productCatalog
from product import Product
from payment_gateway import UPIPayment,NetBanking
from order import order
if __name__=="__main__":
    user1=User("madhu","13, abc street")
    while True:
        print("Welcome to order management system!")
        product1=Product("phone","electronic",2,50000)
        product2=Product("laptop","electronic",2,40000)
        product3=Product("earphone","accesory",2,1200)
        catalog=productCatalog()
        catalog.add_product(product1)
        catalog.add_product(product2)
        catalog.add_product(product3)
        cart=[]
        print("Enter 1 to view products,2 to place order,4 to view order history")
        choice=input()
        if choice=="1":
            catalog.view_product()
        elif choice=="2":
            print("Enter the number of products:")
            number_of_products=int(input())
            
            while number_of_products:
                
                print("Enter the product name:")
                product_name=input()
                print("Enter the product quantity:")
                product_quantity=int(input())
                product=catalog.getproduct(product_name)
                if not product.is_available(product_quantity):
                    print("Product is not available!")
                product_item={"product":product,"quantity":product_quantity}
                cart.append(product_item)
                number_of_products=number_of_products-1
            print("Prodducts added to the cart!")
            print("Confirm, do you want to place order(Yes/No)")
            confirmation=input()
            if confirmation=="Yes":
                print("Payment method: UPI/Net Banking")
                payment_method=input()
                if payment_method=="UPI":
                    order1=order(1,cart,user1,UPIPayment())
                    order1.place_order()
                    print(order1.user.order_history)
                else:
                    print("Enter your card number:")
                    card_number=input()
                    order1=order(1,cart,user1,NetBanking(card_number))
                    order1.place_order()

        elif choice=="4":
            user1.view_order_history()
        else:
            break

            