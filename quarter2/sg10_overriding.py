class Animals: #Creates parent class
    def __init__(self, name):
        self.name = name
    def eat(self):
        pass
    def make_sound(self):
        pass

class Lion(Animals): #Creates child class
    def make_sound(self):
        return f"{self.name} roars loudly!"
    def eat(self):
        return f"{self.name} eats fresh meat."
    feed = eat

class Elephant(Animals): #Creates child class
    def make_sound(self):
        return f"{self.name} trumpets!"
    def eat(self):
        return f"{self.name} eats grass and fruits."
    feed = eat

class Monkey(Animals): #Creates child class
    def make_sound(self):
        return f"{self.name} chatters!"
    def eat(self):
        return f"{self.name} eats bananas."
    feed = eat

if __name__ == "__main__": 
    lion_ = Lion("Simba")
    elephant_ = Elephant("Dumbo")
    monkey_ = Monkey("George")

    print(lion_.make_sound())
    print(lion_.feed())
    print("-----")

    print(elephant_.make_sound())
    print(elephant_.feed())
    print("-----")

    print(monkey_.make_sound())
    print(monkey_.feed())
    print("-----")
