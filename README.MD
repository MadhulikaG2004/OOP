# Order Management System

## class

## User - contains user attributes
## Product -contains product attributes
## Product Catalog - Manages the product 
## Order - has User and Payment Gateway
## Payment Gateway - abstract class 
## UPI and NetBanking implements Payment Gateway class

* Abstraction - payment gateway class hides complexity, defines initiate payment method
* Encapsulation - payment gateway class restricts access to the card number attribute

## Relation

* aggregation (has-a)- product catalog contains product,order has product [whole-part]
* Dependency Injection - order depends on payment gateway
* association - order has user (can exist independently)
