### 1. Answers to the Questions

**a. What is duck typing, as explained in the video?**
Duck typing in Python is when an object's suitability is determined by its methods and properties, rather than its class or type. It allows polymorphism without requiring classes to share a parent class.

**b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?**
The Car class only needs to have the same method name as the Dog and Cat classes used inside the loop. Because it shares the same method name, it can be executed properly alongside them.

---

### 2. Code

```python
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car_move = Car()
boat_move = Boat()
drone_move = Drone()

start_trip(car_move)
start_trip(boat_move)
start_trip(drone_move)
```

---

### 3. How does the code in 2.2 demonstrate polymorphism?
This code demonstrates polymorphism because a single function (startTrip(vehicle)) accepts objects from different classes. and calls the same method on each. producing different outputs depending on the object's class.

startTrip(car_move)
startTrip(boat_move)
startTrip(drone_move)


