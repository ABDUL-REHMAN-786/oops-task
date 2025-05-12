# Task 1.1: Create a Car Class
# Create a class named Car with the following:
# • Attributes: brand, color
# • Method: display_info() to print brand and color
# Create two objects of Car with different values and display their info.

# Define the Car class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

# Create two objects of the Car class
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Display information of both cars
car1.display_info()
car2.display_info()

# Output:

Brand: Toyota, Color: Red
Brand: Honda, Color: Blue


# Let's extend the Car class to include additional attributes: 
# model_year and engine_type. Here's the updated version:

# Define the extended Car class
class Car:
    def __init__(self, brand, color, model_year, engine_type):
        self.brand = brand
        self.color = color
        self.model_year = model_year
        self.engine_type = engine_type

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Model Year: {self.model_year}, Engine Type: {self.engine_type}")

# Create two objects of the Car class with extended attributes
car1 = Car("Toyota", "Red", 2022, "Hybrid")
car2 = Car("Honda", "Blue", 2023, "Petrol")

# Display information of both cars
car1.display_info()
car2.display_info()

# Output:

Brand: Toyota, Color: Red, Model Year: 2022, Engine Type: Hybrid
Brand: Honda, Color: Blue, Model Year: 2023, Engine Type: Petrol
