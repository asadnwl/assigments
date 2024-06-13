import random

# Question No 01
print("Question No: 01\n")

def isIN(str1, str2):
    if (str1 in str2) or (str2 in str1):
        show = True
    else:
        show = False
    return show

print(isIN("World!", "Hello World"))
print(isIN("World", "Hello World!"))
print(isIN("Hello World!", "World"))

# Question No 02
print("Question No: 02\n")

def primeFactor(num):
    
    factor = []
    diviser = 2

    while num > 1:
        while num % diviser == 0:
            factor.append(diviser)
            num //= diviser
        diviser += 1
    return factor

number = 21
ans = primeFactor(number)
print(f"The prime factor of {number} are {ans}")

# Question No 03
print("Question No: 03\n")

def check_number_armstrong(num):
    sum_num = 0
    for i in num:
        numInt = int(i)
        digit = numInt % 10
        sum_num += digit ** 3

    if sum_num == int(num):
        return(f"{num} is an Armstrong number.")
    else:
        return(f"{num} is not an Armstrong number.")

number =  input("Add number: ")
print(check_number_armstrong(number))

# Question No 04
print("Question No: 04\n")

def get_octal_equivalent(decimal_number):
    octal_digit = ""

    while decimal_number > 0:
        remainder = str(decimal_number % 8)
        octal_digit += remainder
        decimal_number //= 8
    octal_number = octal_digit[::-1]
    return octal_number

print(get_octal_equivalent(50))

# Question No 05
print("Question No: 05\n")

def range_fun(start, stop, step):
    number = []

    while start < stop:
        number.append(start)
        start += step
    return number

print(range_fun(2, 11, 2))

# Question No 06
print("Question No: 06\n")

def binary2Decimal(binary_number):
    decimal_number = 0
    index = 0

    while index < len(binary_number):
        digit = int(binary_number[-(index+1)])
        decimal_number += (2 ** index) * digit
        index +=1
    return decimal_number
    
print(binary2Decimal("1011"))

# Question No 07
print("Question No: 07\n")

def multiple(first_integer, second_integer):

    if  second_integer % first_integer == 0:
        return True
    else:
        return False
    
print(multiple(7, 16))

# Question No 08
print("Question No: 08\n")

def solid_square_character(integer, character):

    for i in range(integer):
        print(character * integer)
        i += i

solid_square_character(5, "#")

# Question No 09
print("Question No: 09\n")

def celsius_to_fahrenheit(celsius):
    return round(celsius * (9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenhiet):
    return round(fahrenhiet - 32 * (5/9), 1)

print("celsius\t|\tfahrenhiet")
for celsius in range(0, 101):
    print(f"  {celsius}\t|\t  {celsius_to_fahrenheit(celsius)}")

print("\n")

print("fahrenhiet\t|\tCelsius")
for fahrenhiet in range(32, 213):
    print(f"    {fahrenhiet}\t\t|\t {fahrenheit_to_celsius(fahrenhiet)}")

# Question No 10
print("Question No: 10\n")

def perfect_number(number):
    
    divisor = 0

    for i in range(1, number):
        if number % i == 0:
            divisor += i
            i += 1
    if divisor == number:
        print(f"{number} is a perfect number.")

for i in range(1, 1001):
    perfect_number(i)

# Question No 11
print("Question No: 11\n")

count_head = 0
count_tail = 0

for i in range(1, 101):
    a = random.randint(0,1)

    if a == 1:
        count_head += 1
    else:
        count_tail += 1

print(f"Number of heads: {count_head}, Number of tails: {count_tail}")

# Question No 12
print("Question No: 12\n")

numbers = 0
num_list = []

for i in range(1, 11):
    num = random.randint(1, 100)
    num_list.append(num)
    numbers += num 


mean = numbers / 10
a = sorted(num_list)
median_index = int(10 / 2)
median = (a[median_index] + a[median_index-1]) / 2

print(f"The median of random 10 numbers are {median}")
print(f"The mean of random 10 numbers are {mean}")

# Question No 13
print("Question No: 13\n")

ls = [3,5,3,4,23,43,54,23,70,65]
new_ls = []

[new_ls.append(i) for i in ls if i not in new_ls]

print(new_ls)

# Question No 14
print("Question No: 14\n")

def minimum_number(tuple_param):
    min_num = tuple_param[0]

    for i in tuple_param:
        if i < min_num:
            min_num = i
    return(min_num)

my_tuple = (12,34,22,24,553,8,54,232,53,54)

print(minimum_number(my_tuple))

# Question No 15
print("Question No: 15\n")

my_list = []

for i in range(1, 11):
    a = input("Enter your name: ")
    b = int(input("Enter your marks: "))
    my_list.append(a)
    my_list.append(b)

print(my_list)

# Question No 16
print("Question No: 16\n")

valid_users = ['Ahmad', 'Zainab', 'Hina', 'Ali']

login_ID = input("Enter a login ID: ")

if login_ID in valid_users:
    print(f">>>\nLogin: {login_ID}\nYou are in!\nDone")
else:
    print(f"User ID {login_ID} is not valid.")

# Question No 17
print("Question No: 17\n")

def swap(list_name, first_index, second_index):
    list_name[first_index], list_name[second_index] = list_name[second_index], list_name[first_index]

my_list = []

for i in range(1, 11):
    name = input("Enter names: ")
    my_list.append(name)

swap(my_list, 0, i-1)
print(my_list)

# Question No 18
print("Question No: 18\n")

my_list = ['January', 'February', 'March']

for i in range(len(my_list)):
    word = my_list[i][:3]
    print(word)


# Question No 19
print("Question No: 19\n")

def twoDlist(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("This multiplication in not possible.")
        return None
    
    result_matrix = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix

matrix1 = [
    [2, 3, 1],
    [9, 1, 5],
    [3, 5, 2]
]

matrix2 = [
    [4, 6, 1],
    [7, 0, 4],
    [3, 9, 8]
]

result = twoDlist(matrix1, matrix2)

if result:
    for row in result:
        print(row)


# Question No 20
print("Question No: 20\n")

n = int(input("Enter n: "))
new_list = []

for i in range(n):
        new_list.append((i ** 2))
    
print(new_list)

# Question No 21
print("Question No: 21\n")

def ion2e(word, a = "ion", b = "e"):
    new_word = word.replace(a, b)
    return new_word

changing_word = input("Enter a word: ")

print(ion2e(changing_word))