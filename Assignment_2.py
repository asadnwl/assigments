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