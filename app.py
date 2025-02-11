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
#     print("---------------------------------" )  