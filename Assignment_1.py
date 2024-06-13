from itertools import combinations


# Question No 01
print("Question No: 01\n")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

# Print sum of a & b
sum = a + b
print(f"The sum of {a} and {b} is: {sum}")

# Print the product of a & b
product = a * b
print(f"The product of {a} and {b} is: {product}")

# Print Difference of a & b
difference = a - b
print(f"The difference of {a} and {b} is: {difference}")

# Print quotient of a & b
try:
    quotient = a / b
    print(f"The quotient of {a} and {b} is: {quotient}")
except Exception as e:
    print(e)

# Print remainder of a & b
try:
    remainder = a % b
    print(f"The remainder of {a} and {b} is: {remainder}")
except Exception as e:
    print(e)

# Question No 02
print("\nQuestion No: 02\n")

distance = int(input("Enter distance in Km: "))

# In meters(m)
inmeters = distance * 1000
print(f"{distance} km in meters = {inmeters} m")

# In centimeters
incentimeters = inmeters * 100
print(f"{distance} km in centimeters = {incentimeters} cm")

# In inch
ininch = incentimeters / 2.54
roundinch = round(ininch, 2)
print(f"{distance} km in inch = {roundinch} in")

# In feet
infeet = ininch / 12
roundfeet = round(infeet, 2)
print(f"{distance} km in feet = {roundfeet} ft")

# Question No: 03
print("\nQuestion No: 03\n")

# Get obtain marks from users
eng = int(input("Enter the obtain marks of English: "))
urdu = int(input("Enter the obtain marks of Urdu: "))
math = int(input("Enter the obtain marks of Math: "))
phy = int(input("Enter the obtain marks of Physics: "))
com = int(input("Enter the obtain marks of Computer: "))

# Obtain marks
totalmarks = 100 * 5
obtainmarks = eng + urdu + math + phy + com
print(f"\nStudent obtain {obtainmarks} marks out of {totalmarks}")

# percentage
percentage = (obtainmarks / totalmarks) * 100
print(f"Student get {percentage}% marks")

# Question No: 04
print("\nQuestion No: 04\n")

# Get temperature in fahrenheit
tempinfahrenheit = int(input("Enter temperature in fahrenheit(f):"))

# covert into centigrade
tempincentigrade = round((tempinfahrenheit - 32) * (5 / 9), 1)
# roundcentigrade = round(tempincentigrade, 1)
print("Temperature of", tempinfahrenheit, "f in centigrade is", tempincentigrade,"C")

# Question No: 05
print("\nQuestion No: 05\n")

# Get length & width from user
length = float(input("Enter length of a rectangle in meter: "))
width = float(input("Enter width of rectangle in meter: "))

# Area of rectangle
area = length * width
print(f"Area of rectangle is {area} meter square")

# Perimeter of rectangle
perimeter = (2 * length) + (2 * width)
print(f"Perimeter of rectangle is {perimeter} meter")

# Question No: 06
print("\nQuestion No: 06\n")

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

times = base ** exponent
print(f"The {base} of times is: {times}")

# Question No: 07
print("\nQuestion No: 07\n")

num = int(input("Enter 5 digit number: "))
numssum = 0

while num > 0:
    digit = num%10
    numssum += digit
    num = int(num/10)

print(numssum)

# Question No: 08
print("\nQuestion No: 08\n")

PI = 3.14159
radius = float(input("Enter radius of a circle: "))

print("Diameter of circle is %f", 2*radius)
print("Circumference of circle is %f", (2*PI*radius))
print("Area of circle is %f", (PI*(radius**2)))

# Question No: 09
print("\nQuestion No: 09\n")

maritalstatus = input("Enter 'M' for married or 'U' for unmarried: ").capitalize()

if maritalstatus == "M":
    print("The driver must be insured.")

elif maritalstatus == "U":
    sex = input("Enter 'M' for male or 'F' for female: ").capitalize()
    age = int(input("Enter your age: "))

    if sex == "M" and age > 30:
        print("The driver must be insured.")
    elif sex == "F" and age > 25:
        print("The driver must be insured.")

else:
    print("The driver cannot be insured.")

# Question No: 10
print("\nQuestion No: 10\n")

year = int(input("Enter year for check: "))

if year % 4 == 0:
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Question No: 11
print("\nQuestion No: 11\n")

num = int(input("Enter number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Question No: 12
print("\nQuestion No: 12\n")

firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))

if firstnum % secondnum == 0:
    print(f"{firstnum} is the multiple of {secondnum}")
else:
    print(f"{firstnum} is not a multiple of {secondnum}")

# Question No: 13
print("\nQuestion No: 13\n")

firstnums = int(input("Enter first number: "))
secondnums = int(input("Enter second number: "))

if firstnums > secondnums:
    print(f"{firstnums} is larger.")
elif firstnums == secondnums:
    print("These numbers are equal.")
else:
    print(f"{secondnums} is larger.")

# Question No: 14
print("\nQuestion No: 14\n")

num1, num2, num3 = map(int, input("Enter three different integers: ").split())

sum = num1 + num2 + num3
print(f"Sum is {sum}")

average = sum / 3
roundaverage = round(average, 3)
print(f"Average is {roundaverage}")

product = num1 * num2 * num3
print(f"Product is {product}")

if num1 < num2:
    if num1 < num3:
        print(f"Smallest is {num1}")
    else:
        print(f"Smallest is {num3}")
elif num2 < num3:
    print(f"Smallest is {num2}")
else:
    print(f"Smallest is {num3}")

if num1 > num2:
    if num1 > num3:
        print(f"Largest is {num1}")
    else:
        print(f"Largest is {num3}")
elif num2 > num3:
    print(f"Largest is {num2}")
else:
    print(f"Largest is {num3}")

# Question No: 15
print("\nQuestion No: 15\n")

weightinkg = float(input("Enter weight in killograms: "))
heightinm = float(input("Enter height in meters: "))

BMI = weightinkg / (heightinm * heightinm)
roundBMI = round(BMI, 2)
print(f"Body mass index is {roundBMI}")

if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")

# Question No: 16
print("\nQuestion No: 16\n")

angle1, angle2, angle3 = map(int, input("Enter three angles of triangle: ").split())

angle_sum = angle1 + angle2 + angle3

if angle_sum == 180:
    print("This triangle is valid.")
else:
    print("This triangle is not a valid triangle.")

# Question No: 17
print("\nQuestion No: 17\n")

length = float(input("Enter length of a rectangle: "))
width = float(input("Enter breadth of rectangle: "))

area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)

if area_of_rectangle > perimeter_of_rectangle:
    print("Area of the rectangle is greater than its perimeter")
else:
    print("Area of the rectangle is smaller than its perimeter")

# Question No: 18
print("\nQuestion No: 18\n")

number_of_days = int(input("Enter the number of days: "))

if number_of_days <= 5:
    print("Late returning book fine is 50 paise.")
elif number_of_days <= 10:
    print("Late returning book fine is One rupee.")
elif number_of_days > 10 and number_of_days <= 30:
    print("Late returning book fine is 5 rupees.")
else:
    print("Your membership is cancelled.")

# Question No: 19
print("\nQuestion No: 19\n")

side1, side2, side3 = map(int, input("Enter three sides of a triangle: ").split())

if side1 == side2 == side3:
    print("Triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("The triangle is isosceles.")
elif (side1 ** 2) == ((side2 ** 2)+(side3 ** 2)) or (side2 ** 2) == ((side1 ** 2)+(side3 ** 2)) or (side3 ** 2) == ((side2 ** 2)+(side1 ** 2)):
    print("The triangle is right-angled triangle.")
else:
    print("The triangle is scalene.")

# Question No: 20
print("\nQuestion No: 20\n")

A = int(input("Enter the percentage of subject A: "))
B = int(input("Enter the percentage of subject B: "))

if A >= 55 and B >= 45:
    print("The student is passed.")
elif (A >= 55 or A >= 45) and B >= 55:
    print("The student is passed.")
elif A >= 65 and B < 45:
    print("The student can reappear in subject B.")
else:
    print("Student is failed")

# Question No: 21
print("\nQuestion No: 21\n")

print("Number\tSquare\tCube")
for number in range(11):
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")

# Question No: 22
print("\nQuestion No: 22\n")

sum_of_even = 0
for num in range(2, 31):
    if num % 2 == 0:
        sum_of_even += num
print("Sum of even integers from 2 to 30 is ", sum_of_even)

# Question No: 23
print("\nQuestion No: 23\n")

num = int(input("Enter the number of values you want to entered: "))

count_positive = 0
count_negative = 0
count_zero = 0
for _ in range(num):
    nums = int(input("Enter the number: "))
    if nums > 0:
        count_positive += 1
    elif nums < 0:
        count_negative += 1
    else:
        count_zero += 1

print(f"Count of positive Number is {count_positive}\nCount of negative number is {count_negative}\nCount of zero is {count_zero}")

# Question No: 24
print("\nQuestion No: 24\n")

number = int(input("Enter a decimal number: "))

binary_number = ""
while number > 0:
    remainder = number % 2
    binary_number = str(remainder) + binary_number
    number = int(number / 2)
print(binary_number)

# Question No: 25
print("\nQuestion No: 25\n")

number_of_element = int(input("Enter the number of element in set: "))

smallest_number = float("inf")
largest_number = float("-inf")

for _ in range(number_of_element):
    number = float(input("Enter number: "))
    if number < smallest_number:
        smallest_number = number
    elif number > largest_number:
        largest_number = number

range_of_number = largest_number - smallest_number
print(range_of_number)

# Question No: 26
print("\nQuestion No: 26\n")

a = ["1", "2", "3"]

for r in range(1, len(a)+1):
    for l in combinations(a, r):
        print(l)

# Question No: 27
print("\nQuestion No: 27\n")

number_of_employees = int(input("Enter the number of employees: "))

for _ in range(number_of_employees):
    working_hours = int(input("Enter # of hours worked: "))
    hourly_rate = float(input("Enter hourly rate of the worker: "))

    if working_hours > 40:
        overtime_hours = working_hours - 40
        regular_pay = 40 * hourly_rate
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        net_salary = regular_pay + overtime_pay
    else:
        net_salary = working_hours * hourly_rate

    print(f"Salary is ${net_salary}")

# Question No: 28
print("\nQuestion No: 28\n")

factorial_number = int(input("Enter factorial number: "))

product_of_numbers = 1
for i in range(factorial_number, 0, -1):
    product_of_numbers *= i
print(product_of_numbers)

# Question No: 29
print("\nQuestion No: 29\n")



# Question No: 30
print("\nQuestion No: 30\n")

number = int(input("Enter a number: "))

for i in range(number):
    print("*" * number)

# Question No: 31
print("\nQuestion No: 31\n")

print("*******")
for _ in range(5):
    print("********")
    print(" ********")

# Question No: 32
print("\nQuestion No: 32\n")

for i in range(1, 11):
    print("*" * i)
for i in range(10, 0, -1):
    print("*" * i)
for i in range(10, 0, -1):
    print((" " * (10-i))+("*" * i))
k = 10
for i in range(11):
    print(" " * (k//2) + "*" * (i))
    k = k-1

# Question No: 33
print("\nQuestion No: 33\n")

def original_expression_a(x, y):
    return not(x < 5) and not(y >= 7)
def original_expression_b(a, b, g):
    return not(a == b) or not(g != 5)
def original_expression_c(x, y):
    return not((x <= 8) and (y > 4))
def original_expression_d(i, j):
    return not((i > 4) or (j <= 6))

def equivalent_expression_a(x, y):
    return not((x < 5) or (y >= 7))
def equivalent_expression_b(a, b, g):
    return not((a == b) and (g != 5))
def equivalent_expression_c(x, y):
    return not(x <= 8) or not(y > 4)
def equivalent_expression_d(i, j):
    return not(i > 4) and not(j <= 6)

original_result_a = original_expression_a(3, 8)
original_result_b = original_expression_b(2, 5, 5)
original_result_c = original_expression_c(8, 6)
original_result_d = original_expression_d(1, 7)

equivalent_result_a = equivalent_expression_a(3, 8)
equivalent_result_b = equivalent_expression_b(2, 5, 5)
equivalent_result_c = equivalent_expression_c(8, 6)
equivalent_result_d = equivalent_expression_d(1, 7)

print(f"Original expression result: {original_result_a}\t Equivalent expression result: {equivalent_result_a}\t Test Result: {original_result_a == equivalent_result_a}")
print(f"Original expression result: {original_result_b}\t Equivalent expression result: {equivalent_result_b}\t Test Result: {original_result_b == equivalent_result_b}")
print(f"Original expression result: {original_result_c}\t Equivalent expression result: {equivalent_result_c}\t Test Result: {original_result_c == equivalent_result_c}")
print(f"Original expression result: {original_result_d}\t Equivalent expression result: {equivalent_result_d}\t Test Result: {original_result_d == equivalent_result_d}")

# Question No: 34
print("\nQuestion No: 34\n")

for i in range(1, 5):
    print("*" * i)
for i in range(5, 0, -1):
    print("*" * i)