class Human:
    # Class Attributes
    species = "Homo-Sapiens"

    # Class Constructors
    def __init__(self, name, age):
        if not name:
            raise ValueError("Name cannot be empty.")
        if age<0 or age>100:
            raise ValueError("Age must be between 0 and 100.")

        self.name = name # Instance attribute
        self.age = age

# Creating an object of a class
human1 = Human("Tanmay", 22)
print(human1.name)
print(human1.age)