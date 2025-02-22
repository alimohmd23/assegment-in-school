'''
workshop 1
'''
# Question 1: Write a Python program that:
# 1. Declares two variables: num1 and num2 and assigns them integer values of 5
# and 6, respectively.
# 2. Calculates the sum of num1 and num2 and stores the result in a variable called
# result.
# 3. Prints the calculated sum to the console in three different ways:
# o Directly print the value of the result variable.
# o Print the sum as a string using string concatenation.
# o Print the sum using f-string formatting.

# num1 = 5
# num2 = 6
# result = num1 + num2
# print("The sum is:", result)
# print("The sum is: " + str(result))
# print(f"The sum is: {result}")

# name = "ali" 
# score = 95
# print(f"{name} scored {score} points in the game.")

# Question 2: Write a Python program that takes two numbers as input from the
# user. The program should:
# 1. Attempt to add the two numbers directly without any type conversion.
# 2. Then, convert both input values to integers and perform the addition.
# 3. Finally, convert both input values to floating-point numbers and perform
# the addition.
# Print the result of each addition operation in a clear and readable format.

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# result = num1 + num2
# print("The sum is:", result)
# result = int(num1) + int(num2)
# print("The sum is:", result)
# result = float(num1) + float(num2)
# print("The sum is:", result)

# Question 3: Write a Python program that classifies an employee's performance
# based on their performance rating.
# Requirements:
# • Create a variable named employee to store the employee's name.
# • Create a variable named rate to store the employee's performance rating (a
# number between 1 and 5, where 5 is the highest).
# • Implement the following rating system:
# o If the rate is 5 or higher, print "Your Rate Is Excellent".
# o If the rate is between 3 and 4 (inclusive), print "Your Rate Is Good".
# o If the rate is between 2 and 2.99, print "Your Rate Is Bad".
# o If the rate is below 2, print "Your Rate Is Very Bad".
# Example:
# If employee is "Ramy" and rate is 5, the output should be:
# Your Rate Is Excellent"

# name = input("Enter your name: ")
# rate = int(input("Enter your performance rating: ")) 
# if rate >= 5:
#     print(f"{name}, Your Rate Is Excellent")
# elif 3 <= rate <= 4:
#     print(f"{name}, Your Rate Is Good")
# elif 2 <= rate < 3:
#     print(f"{name}, Your Rate Is Bad")
# else:
    # print(f"{name}, Your Rate Is Very Bad")

# Question 4: Print Multiplication Table
# Write a Python program that prints the multiplication table of a given number
# using a for loop.
# Requirements:
# • Create a variable num to store the input number.
# • Use a for loop with range() to iterate from 1 to 10.
# • Print the multiplication table in the format: {num} x {i} = {result}.
# Example Output (for num = 3):
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ...
# 3 x 10 = 30

# num = int(input("Enter a number: ")) 
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
    
# Question 5: Sum of Even Numbers
# Write a Python program that calculates the sum of even numbers from 1 to n
# using a for loop.
# Requirements:
# • Create a variable n to store the input number.
# • Use a for loop with range() to iterate from 1 to n.
# • Add only even numbers to the sum.
# • Print the total sum at the end.
# Example Output (for n = 10):
# The sum of even numbers from 1 to 10 is 30.

# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total += i
# print(f"The sum of even numbers from 1 to {n} is {total}.")

# Question 6: Countdown Using a While Loop
# Write a Python program that takes a number and counts down to 0 using a while
# loop.
# Requirements:
# • Create a variable num to store the input number.
# • Use a while loop to decrease the value of num until it reaches 0.
# • Print each number during the countdown.
# Example Output (for num = 5):
# 5
# 4
# 3
# 2
# 1
# 0
# Countdown complete!

# num = int(input("Enter a number: "))
# while num >= 0:
#     print(num)
#     num -= 1
# print("Countdown complete!")

# Question 7: Password Guessing Program
# Write a Python program that asks the user to enter a password. The program
# should keep asking until the correct password is entered.
# Requirements:
# • Set a variable correct_password = "Python123".
# • Use a while loop to repeatedly ask for user input.
# • If the input matches correct_password, print "Access Granted!" and exit
# the loop.
# Example Output:
# Enter password: hello123
# Incorrect password, try again.
# Enter password: Python123
# Access Granted!

# correct_password = "python123"
# while True:
#     user_input = input("Enter password: ")
#     if user_input == correct_password:
#         print("Access Granted!")
#         break
#     else:
#         print("Incorrect password, try again.")

# Question 8: Sum of List Elements
# Write a Python program that calculates the sum of all numbers in a list.
# Example:
# numbers = [10, 20, 30, 40, 50]
# Expected Output:
# Sum of numbers: 150

# numbers = [10, 20, 30, 40, 50]
# sum_of_numbers = sum(numbers)
# print(f"Sum of numbers: {sum_of_numbers}")

# Question 9: Find Maximum and Minimum in a List
# Write a Python program that finds the maximum and minimum values in each
# list.
# Example:
# numbers = [23, 1, 56, 3, 98, 45]
# Expected Output:
# Maximum: 98
# Minimum: 1

# numbers = [23, 1, 56, 3, 98, 45]
# max = max(numbers)
# min = min(numbers)
# print(f"Maximum: {max}")
# print(f"Minimum: {min}")

# Question 10: Access Dictionary Values
# Write a Python program that prints the value of a specific key from a dictionary.
# Example:
# student = {"name": "Mohamed", "age": 16, "grade": "A"}
# Expected Output (for key "age"):
# The student's age is 16.

# student = {"name": "Mohamed", "age": 16, "grade": "A"}
# key = "age"
# value = student[key]
# print(f"The student's {key} is {value}.")

# Question 11: Iterate Over a Dictionary
# Write a Python program that prints all keys and values in a dictionary using a
# loop.
# Example:
# student = {"name": "Ahmed", "age": 15, "grade": "B"}
# Expected Output:
# name: Ahmed
# age: 15
# grade: B

# student = {"name": "Ahmed", "age": 15, "grade": "B"}
# for key, value in student.items():
#     print(f"{key}: {value}")

# Question 12: Store and Display Car Information to Represent each car as a
# dictionary and store all car dictionaries in a list.
# Write a Python program that represents each car as a dictionary and stores all
# car dictionaries in a list.
# • Create a list of dictionaries called cars, where each dictionary represents a
# car and contains the following keys:
# o "name" (car model)
# o "color" (car color)
# o "price" (car price)
# o "speed" (maximum speed)
# • Use a loop to iterate through the cars list and print each car’s details.

# cars = [
#     {"name": "Toyota Camry", "color": "Blue", "price": 25000, "speed": 180},
#     {"name": "Tesla Model S", "color": "Red", "price": 80000, "speed": 250},
#     {"name": "Ford Mustang", "color": "Black", "price": 45000, "speed": 220},
#     {"name": "Honda Civic", "color": "White", "price": 22000, "speed": 160},
# ]
# for car in cars:
#     print(f"Car Model: {car['name']}")
#     print(f"Color: {car['color']}")
#     print(f"Price: ${car['price']}")
#     print(f"Max Speed: {car['speed']} k/h")
#     print(f"Min Speed: {car['speed']} m/s")
#     print("-" * 40)  

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''
workshop 2
'''


# Question 1: Convert Currency (USD to EUR)
# Scenario:Write a Python function named usd_to_eur that takes two arguments:
# 1. amount: The amount of money in US Dollars (USD).
# 2. exchange_rate: The exchange rate from USD to EUR. This argument should
# have a default value of 0.85.
# The function should return the equivalent amount of money in Euros (EUR) by
# multiplying the amount by the exchange_rate."

# print("If you need to convert USD to EUR enter 1")
# print("If you need to convert EUR to USD enter 2")

# def exchange():
#     while True:
#         x = int(input("Enter number: "))
#         if x in [1, 2]:
#             break
#         print("Please enter 1 or 2")

#     if x == 1:
#         amount = float(input("Please enter the amount of USD: "))
#         exchange_rate = 0.85
#         result = amount * exchange_rate
#         print(f"The amount in EUR is: {result}")
#     elif x == 2:
#         amount = float(input("Please enter the amount of EUR: "))
#         exchange_rate = 1.18
#         result = amount * exchange_rate
#         print(f"The amount in USD is: {result}")
# exchange()


# Question 2: Calculate Total Bill with Tax
# Scenario: Write a Python function named calculate_total that takes the price of an
# item and the tax rate as input. The function should calculate and return the total price
# of the item including tax.
# Example: If the price of an item is $100 and the tax rate is 7%, the function should
# return $107.00."

# def calculate(price, tax):
#     total = price + (price * tax / 100)
#     return total
# price = float(input("Enter the price of the item: "))
# tax = 7
# total = calculate(price, tax)
# print(f"The total price including tax is: ${total:.2f}")


# Question3: Find the Maximum of Three Numbers
# Scenario: Write a Python function named find_largest that takes three numbers as
# input. The function should determine and return the largest of the three numbers.
# Example: If the input numbers are 10, 5, and 15, the function should return 15.

# def find_largest(num1, num2, num3):
#     return max(num1, num2, num3)
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# largest = find_largest(num1, num2, num3)
# print(f"The largest number is: {largest}")

# Question 4: Create a Python class named Car that represents the
# properties of a car.
# Scenario: Create a Python class named Car that represents the properties of a car.
# The class should have the following attributes:
# • name: The name of the car model (e.g., "Car1", "Sedan", "SUV")
# • color: The color of the car (e.g., "Red", "Blue", "Black")
# • price: The price of the car (e.g., 20000, 30000)
# • speed: The maximum speed of the car (e.g., 150, 180)
# The class should also have an __init__ method (constructor) that takes these
# arguments and initializes the corresponding attributes for each car object.

# class Car:
#     def __init__(self, name, color, price, speed):
#         self.name = name
#         self.color = color
#         self.price = price
#         self.speed = speed
#     def display_info(self):
#         print(f"Car Model: {self.name}")
#         print(f"Color: {self.color}")
#         print(f"Price: ${self.price}")
#         print(f"Max Speed: {self.speed} k/h")
#         print("-" * 40)
# car1 = Car("Toyota Camry", "Blue", 25000, 180)
# car2 = Car("Tesla Model S", "Red", 80000, 250)
# car3 = Car("Ford Mustang", "Black", 45000, 220)
# car4 = Car("Honda Civic", "White", 22000, 160)
# car1.display_info()
# car2.display_info()
# car3.display_info()
# car4.display_info()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

Workshop 3

'''

# Question 1: Create a Python class named Robot that represents the attributes of a
# robot.
# Scenario: The class should have the following attributes:
# • name: The name of the robot (, "Laziz", "Zumba", "Droid")
# • color: The color of the robot ("red", "blue", "green")
# The class should also have an __init__ method (constructor) that takes these
# arguments and initializes the corresponding attributes for each robot object.
# After creating the class, instantiate an object of the Robot class with the name
# "Zumba" and color "red". Print the name and color of the created robot object.

# class Robot:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# zumba = Robot("Zumba", "red")
# Laziz = Robot("Laziz", "blue")
# Droid = Robot("Droid", "green")
# print(f"Robot Name: {zumba.name}, Color: {zumba.color}")
# print(f"Robot Name: {Laziz.name}, Color: {Laziz.color}")
# print(f"Robot Name: {Droid.name}, Color: {Droid.color}")

# Question 2: Create a Python class named Smartphone that represents the
# properties of a smartphone.
# Scenario: The class should have the following attributes:
# • brand: The brand of smartphone ("Apple", "Samsung")
# • model: The model of the smartphone ("iPhone 12", "Galaxy S21")
# The class should also have:
# • An __init__ method (constructor) that takes brand and model as arguments and
# initializes them for each smartphone object.
# • A method named display_info that prints the brand and model of the
# smartphone.
# Create an object of the Smartphone class and call the display_info method to display
# the smartphone details.
# Both solutions define a Smartphone class, initialize its properties using a constructor,
# and include a method to display the smartphone details.

# class Smartphone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display_info(self):
#         print(f"Brand: {self.brand} | Model: {self.model}")
#         print("-" * 40)
# phone1 = Smartphone("Apple", "iPhone 12")
# phone2 = Smartphone("Samsung", "Galaxy S21")
# phone1.display_info()
# phone2.display_info()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Workshop4
'''

# Question 1: Create a Python and JavaScript class named Student that represents
# student information. The class should include:
# Class Attribute:
# • school_name: Represents the name of the school (e.g., "WE-School").
# Instance Attributes:
# • name: The student's name (e.g., "Ahmed", "Ali").
# • grade: The student's grade (e.g., "2nd", "3rd").
# Methods:
# • display_info(): Displays the student's name, grade, and the school name.
# Create two student objects and call the display_info() method to print their
# details.

# class Student:
#     school_name = "WE-School"
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Grade: {self.grade}")
#         print(f"School Name: {Student.school_name}")
#         print("-" * 40)
# student1 = Student("Ahmed", "2nd")
# student2 = Student("Ali", "3rd")
# student1.display_info()
# student2.display_info()


# Question 2: Create a Python class named Book that represents a book in a
# library. The class should include the following:
# 1. Attributes:
# o title (string): The title of the book.
# o author (string): The name of the author.
# o is_borrowed (boolean): A flag to track whether the book is borrowed
# (default should be False).

# 2. Methods:
# o borrow_book(): Marks the book as borrowed if it is available. If the
# book is already borrowed, print a message indicating that it is not
# available.
# o return_book(): Marks the book as returned if it was borrowed. If the
# book was not borrowed, print a message indicating that it was not
# borrowed.

# Finally, create an instance of the Book class with the title "Python
# Programming" and author "Ahmed Ali". Demonstrate borrowing and returning
# the book by calling the respective methods.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False

#     def borrow_book(self):
#         if not self.is_borrowed:
#             self.is_borrowed = True
#             print(f'You have borrowed "{self.title}" by {self.author}.')
#         else:
#             print(f'Sorry, "{self.title}" is already borrowed.')

#     def return_book(self):
#         if self.is_borrowed:
#             self.is_borrowed = False
#             print(f'You have returned "{self.title}".')
#         else:
#             print(f'"{self.title}" was not borrowed.')

# book1 = Book("Python Programming", "Ahmed Ali")

# book1.borrow_book()
# book1.return_book()
# book1.return_book()
# book1.borrow_book()
# book1.borrow_book()
