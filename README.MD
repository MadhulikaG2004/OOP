
# 🛒 Order Management System

## 📌 Overview

This project implements a simple **Order Management System** to practice **Object-Oriented Programming (OOP)** concepts such as **abstraction, encapsulation, aggregation, association, and dependency injection**.

---

## 🧱 Core Classes

### **User**

* Represents a customer of the system
* Stores user-related attributes (id, name, order history, etc.)

---

### **Product**

* Represents an item available for purchase
* Contains product attributes such as name, price, and stock quantity

---

### **ProductCatalog**

* Manages the collection of products
* Acts as a central repository for available products

---

### **Order**

* Represents a purchase made by a user
* Maintains references to:

  * The user who placed the order
  * The products in the order
  * The payment gateway used for payment

---

### **PaymentGateway (Abstract Class)**

* Defines a common interface for payment processing
* Declares the `initiate_payment()` method
* Hides implementation details of different payment mechanisms

---

### **UPIPayment & NetBankingPayment**

* Concrete implementations of the `PaymentGateway` abstraction
* Provide gateway-specific payment logic

---

## 🎯 OOP Concepts Applied

### **Abstraction**

* `PaymentGateway` hides the complexity of payment processing
* Exposes only the `initiate_payment()` method to the `Order` class

---

### **Encapsulation**

* Sensitive attributes (e.g., card number, account details) are restricted
* Access is controlled via class methods, not direct access

---

### **Aggregation (Has-A Relationship)**

* `ProductCatalog` contains `Product` objects
* `Order` contains a collection of `Product` objects
* Products exist independently of the catalog or order

---

### **Association**

* `Order` is associated with a `User`
* User and Order exist independently of each other

---

### **Dependency Injection**

* `Order` depends on the `PaymentGateway` abstraction
* Payment gateway implementation is injected at runtime
* Enables loose coupling and easy extensibility

---

## 🧠 Design Summary

| Concept              | Applied In                                |
| -------------------- | ----------------------------------------- |
| Abstraction          | PaymentGateway                            |
| Encapsulation        | Payment details                           |
| Aggregation          | ProductCatalog → Product, Order → Product |
| Association          | Order → User                              |
| Dependency Injection | Order → PaymentGateway                    |

