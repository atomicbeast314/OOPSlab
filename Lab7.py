#q1
class person:
    def __init__(self, name, age):  # Correct method definition and parameters
        self.name = name  # Correct variable name
        self.age = age

    def display(self):  # Correct method definition
        print(f"Name: {self.name}, Age: {self.age}")


class student(person):
    def __init__(self, name, age, student_id):  # Correct method definition and parameters
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        self.display()
        print(f"Student ID: {self.student_id}")


student1 = student("Alice", 20, "S12345")
student1.show_details()

#q2
class vehicle:
    def intro(self):  # Corrected method name
        print("This is a vehicle")

class car(vehicle):
    def car_info(self):
        print("This is a car")

class electriccar(car):  # Corrected class name
    def battery_info(self):
        print("This car has a battery")

electric_car = electriccar()  # Corrected class name
electric_car.intro()  # Corrected method call
electric_car.car_info()
electric_car.battery_info()

#q3
class teacher:
    def description(self):
        print("This is a teacher")

class author:
    def description(self):
        print("This is an author")  # Corrected spelling

class tutorauthor(teacher, author):
    def description(self):
        super().description()  # Calls the teacher's description
        author.description(self)  # Calls the author's description

tutor_author = tutorauthor()  # Corrected variable name
tutor_author.description()

#q4
class animal:
    def sound(self):
        print("Animals make sound")

class Dog(animal):
    def sound(self):
        print("Dog barks")

class Cat(animal):  # Corrected class name
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()  # Added parentheses
