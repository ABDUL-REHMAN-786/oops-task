<!-- Understand these Core Concepts:
o Class
o Object
o Instance
o Method
o Attribute
Write 2–3 lines about each concept in your own words (not copy-pasted). This will help you build a strong  -->


Class: A class is like a blueprint or template that defines the structure and behavior (methods and attributes) that the objects created from it will have.

Object: An object is a specific, usable version of a class—like a real item made using a blueprint. It has actual values stored in its attributes.

Instance: An instance is just another term for an object; when you create an object from a class, you're creating an instance of that class.

Method: A method is a function defined inside a class that describes the behaviors or actions that an object of the class can perform.

Attribute: An attribute is a variable stored inside an object; it holds information about the object, such as its properties or state.

# Defining a class
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name          # Attribute
        self.breed = breed        # Attribute

    # A method
    def bark(self):
        print(f"{self.name} says: Woof!")

# Creating an instance (object) of the class
my_dog = Dog("Buddy", "Golden Retriever")

# Using a method of the object
my_dog.bark()


How the concepts are shown:
Class: Dog is the class (the blueprint).

Object: my_dog is an object created from the Dog class.

Instance: my_dog is also called an instance of Dog.

Method: bark() is a method that tells the dog to bark.

Attribute: name and breed are attributes that store data about the dog.
