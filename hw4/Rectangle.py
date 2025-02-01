class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Create an instance
rect = Rectangle(5, 3)

# Output the area
print("Area:", rect.calculate_area())



#AI Promt: 
# I am working on a Python assignment that requires me to create three separate class-based programs:
#Rectangle.py – Define a Rectangle class with length and width attributes and a method to calculate the area.
#Employee.py – Define an Employee class that can increase an employee's salary by a percentage.
#Pet.py – Define a Pet class with an age conversion method and a way to retrieve species lifespan.
#I want to start with Rectangle.py. I understand that I need to:

#Define a class called Rectangle.
#Use the __init__ method to set length and width.
#Create a method calculate_area() that returns length * width.
#Instantiate an object with length=5 and width=3, then print the area.
# Can you walk me through implementing this class step by step, explaining why each part is needed as we go?