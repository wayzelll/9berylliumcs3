# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

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

### 2. Abstraction


### 3. Inheritance


### 4. Polymorphism


## Reflection
