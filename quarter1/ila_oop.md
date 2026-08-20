# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

---

### 1. Encapsulation
- Encapsulation binds properies like name, price, and quantity into one. Still, it keeps its attrivutes to prevent modifications. This prevents the need for too much variables on the code.

```python
class Product:

  def __init__(obj, name: str, price: float, quantity: int):
    obj.name = name
    obj.price = price
    obj.__quantity = quantity  # Private attribute

  def update_stock(obj, amount: int):
    if obj.__quantity + amount >= 0:
      obj.__quantity += amount
```
---  
### 2. Abstraction

Abstraction hides the complex work happening in a function, creating a clean and simple interface. It keeps the program clean, and allow internal system updates without ruining how users interact with the store.  

```python
class Sari_Sari_Store:

  def sell_item(obj, product_name: str, qty: int):
    pass

``` 
### 3. Inheritance
Inheritance allows categories to inherit common attributes from the base class. The 1st or parent class has the foundation, while the 2nd or the child class can copy and revise the code. This prevents redundancy across the code.

```python
class PerishProduct(Product):

  def __init__(
      obj, name: str, price: float, quantity: int, expiration_date: str
  ):
    super().__init__(name, price, quantity)
    obj.expiration_date = expiration_date

  def is_expired(obj) -> bool:
    return False
```

### 4. Polymorphism
Polymorphism enables different product types to implement shared methods in their own unique ways while being managed uniformly. For example, both Product and PerishableProduct can implement a calculate_discount() method, allowing custom clearance discounts on expiring goods. The main store system can iterate through a single list of Product objects and call .calculate_discount() on each without needing complex conditional type-checking logic, greatly improving scalability.

Polymorphism enables different product type to implement shared methods, but in its own ways. The main systejm can iterate through a single list object, and call on each without needing complex logic, improving scalability.

```python
class PerishableProduct(Product):

  def calculate_discount() -> float:
    return self.price * 0.50  # 50% discount for quick sale
```

## Reflection
I conclude that, among the four pillars, encapsulation would be the most useful in improving the sari-sari store inventory system. Managing multiple variables can create confusion, such as negative results in the inventory. Encapsulation guarantees data integrity by grouping attributes to be controlled. 


