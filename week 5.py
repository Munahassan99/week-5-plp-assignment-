# Base class: Smoothie
class Smoothie:
    def __init__(self, name, size, flavor, price):
        self.name = name          # Name of the smoothie
        self.size = size          # Size: Small, Medium, Large
        self.flavor = flavor      # Flavor: Strawberry, Mango, etc.
        self.price = price        # Price in dollars

    def describe(self):
        return f"{self.size} {self.name} ({self.flavor}) - ${self.price}"

    def enjoy(self):
        return f"Yum! Enjoy your {self.name} smoothie 🍓🥤"


# Subclass: SpecialSmoothie inherits from Smoothie
class SpecialSmoothie(Smoothie):
    def __init__(self, name, size, flavor, price, topping):
        super().__init__(name, size, flavor, price)
        self.topping = topping    # Special topping: Boba, Chocolate Chips, etc.

    def describe(self):
        # Overriding the describe method (polymorphism)
        return f"{self.size} {self.name} ({self.flavor}) with {self.topping} - ${self.price}"

    def enjoy(self):
        return f"Delicious! Your special {self.name} smoothie with {self.topping} is ready! 💖"


# Creating objects
classic = Smoothie("Berry Bliss", "Medium", "Strawberry", 6)
special = SpecialSmoothie("Golden Mango Splash", "Large", "Mango", 8, "Boba")

# Using methods
print(classic.describe())
print(classic.enjoy())
print(special.describe())
print(special.enjoy())
