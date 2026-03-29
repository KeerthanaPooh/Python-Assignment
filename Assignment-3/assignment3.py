# Assignment 3 - Nested If Statements

# 1. E-commerce Discount Calculator
amount = float(input("Enter purchase amount: "))
if amount >= 100:
    if amount <= 500:
        discount = amount * 0.10
    else:
        discount = amount * 0.20
else:
    discount = 0
final_amount = amount - discount
print("Discount:", discount)
print("Final Amount:", final_amount)


# 2. Traffic Light Simulation
color = input("\nEnter traffic light color: ").lower()
if color == "red":
    print("Stop.")
else:
    if color == "yellow":
        print("Ready to move.")
    else:
        if color == "green":
            print("Go.")
        else:
            print("Invalid color.")


# 3. Grade Evaluation
marks = float(input("\nEnter marks: "))
if marks >= 50:
    if marks >= 75:
        if marks >= 90:
            print("Grade A")
        else:
            print("Grade B")
    else:
        print("Grade C")
else:
    print("Fail")


# 4. Odd/Even and Divisibility
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even number")
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
else:
    print("Odd number")
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")


# 5. Password Strength
password = input("\nEnter password: ")
length = len(password)
if length >= 5:
    if length >= 8:
        print("Strong password")
    else:
        print("Medium password")
else:
    print("Weak password")


# 6. Electricity Bill
units = float(input("\nEnter units consumed: "))
if units <= 100:
    bill = units * 0.5
else:
    if units <= 200:
        bill = (100 * 0.5) + (units - 100) * 0.75
    else:
        bill = (100 * 0.5) + (100 * 0.75) + (units - 200) * 1
print("Total bill:", bill)


# 7. Loan Eligibility
age = int(input("\nEnter age: "))
income = float(input("Enter monthly income: "))
if age >= 21:
    if age <= 60:
        if income >= 5000:
            print("Eligible for loan")
        else:
            print("Not eligible for loan")
    else:
        print("Not eligible for loan")
else:
    print("Not eligible for loan")


# 8. Temperature Alert
temp = float(input("\nEnter temperature: "))
if temp >= 0:
    if temp <= 20:
        print("Cold weather")
    else:
        if temp <= 30:
            print("Warm weather")
        else:
            print("Hot weather")
else:
    print("Freezing weather")
