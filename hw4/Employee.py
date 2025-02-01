class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        increase_amount = self.salary * (percentage / 100)
        self.salary += increase_amount
        return self.salary

# Create an Employee instance
john = Employee("John", 5000)

# Increase salary by 10%
new_salary = john.increase_salary(10)
print(john.name + "'s new salary: " + str(new_salary))

#AI Promt: 
#In this file, I need to:
#Create a class Employee with name and salary attributes.
#Implement a method increase_salary(percentage) that increases the salary by a given percentage.
#Instantiate an object of Employee where name = 'John' and salary = 5000.
#Call the method to increase John's salary by 10% and print the updated salary.
#I understand that the increase_salary method should take a percentage as input, convert it to a decimal, and multiply it by the salary to get the increase. Then, it should update the salary and return the new value.