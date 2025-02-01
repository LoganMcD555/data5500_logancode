class Pet:
    species_lifespan = {
        "dog": 13,
        "cat": 15,
        "rabbit": 9,
        "parrot": 50
    }

    average_human_lifespan = 80  # Assumed average human lifespan

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def calculate_human_age(self):
        lifespan = self.species_lifespan.get(self.species)
        if lifespan:
            return round((self.age / lifespan) * self.average_human_lifespan, 2)
        return "Unknown"

    def get_average_lifespan(self):
        return self.species_lifespan.get(self.species, "Unknown")

# Create pet instances
pet1 = Pet("Buddy", 4, "dog")
pet2 = Pet("Whiskers", 2, "cat")
pet3 = Pet("Coco", 5, "parrot")

# Print details
for pet in [pet1, pet2, pet3]:
    print(pet.name + " is " + str(pet.age) + " years old, which is " + str(pet.calculate_human_age()) + " in human years.")
    print("Average lifespan of a " + pet.species + ": " + str(pet.get_average_lifespan()) + " years.\n")

#AI Promt:
#In this file, I need to:

#Create a class Pet with name and age attributes.
#Define a class variable called species.
#Implement a method calculate_human_age() to convert pet age to human-equivalent years.
#Implement a method get_average_lifespan(species) that returns an average lifespan for that species.
#Instantiate three different pets with unique names, ages, and species.
#Print their human-equivalent ages and their species' average lifespans.
#I assume I need to store lifespan data in a dictionary where species names map to their average lifespan.

# Can you guide me through implementing this step by step, explaining why each part is necessary?"