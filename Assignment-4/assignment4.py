# Assignment 4 - For Loop Programs

# 1. Employee Salary Increment
salary = 50000
print("1. Employee Salary Increment:")
for year in range(1, 11):
    salary = salary + (salary * 0.05)
    print(f"Year {year}: ₹{salary:.2f}")


# 2. Class Attendance Percentage
total_classes = 25
attended = 18
print("\n2. Attendance Percentage:")
for i in range(1, attended + 1):
    percentage = (i / total_classes) * 100
    print(f"After {i} classes: {percentage:.2f}%")


# 3. Product Discount Prices
prices = [100, 250, 400, 560, 700]
print("\n3. Discounted Prices:")
for price in prices:
    discount_price = price - (price * 0.10)
    print(f"Original: {price}, Discounted: {discount_price}")


# 4. Monthly Savings Growth
savings = 0
print("\n4. Monthly Savings:")
for month in range(1, 13):
    savings += 1000
    print(f"Month {month}: ₹{savings}")


# 5. Electricity Bill Calculation
units_list = [120, 135, 150, 160, 145]
cost_per_unit = 5
print("\n5. Electricity Bills:")
for month, units in enumerate(units_list, start=1):
    bill = units * cost_per_unit
    print(f"Month {month}: ₹{bill}")


# 6. Student Marks Percentage
marks = [78, 85, 90, 66, 72]
print("\n6. Subject Percentages:")
for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}%")
