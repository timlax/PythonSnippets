

class Animal(object):
    """All animals"""
    alive = ""

    # Define the initialisation function to define the self attributes (mandatory in a class creation)
    def __init__(self, name, age):
        # Each animal will have a name and an age
        self.name = name
        self.age = age

    # The description function will print the animals name & age attributes
    def description(self):
        print(self.name)
        print(self.age)

    # The SetAlive function will define the attribute "alive" for an animal as alive
    def setAlive(self, alive):
        self.alive = alive

    # The getAlive function will show the value of the attribute "alive" for an animal
    def getAlive(self):
        return self.alive

# Define your first animal with its values for the "self attributes"
horse = Animal("Hilda", 22)

# Call the description function to print name & age
horse.description()

# Call the setAlive function to define that your animal is alive
horse.setAlive(True)

# Call the getAlive function to know if your animal is alive
print(horse.getAlive())

# Call the setAlive function to define that your animal is NOT alive
horse.alive=False

# Call the getAlive function to know if your animal is alive
print(horse.getAlive())

# Change the value of the age attribute for your selected animal & print the new age
horse.age += 1
print(horse.age)
