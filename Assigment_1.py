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

