import math
n=int(input("Enter a number to find its cube and square: "))
square = math.pow(n, 2)
cube = math.pow(n, 3)
print("The square of", n, "is", square)
print("The cube of", n, "is", cube)

b=int(input("Enter a number to find its factorial: "))
factorial = math.factorial(b)
print("The factorial of", b, "is", factorial)

a=int(input("Enter your first number to find the GCD: "))
b=int(input("Enter your second number to find the GCD: "))
gcd = math.gcd(a, b)
print("The GCD of", a, "and", b, "is", gcd)

c=int(input("Enter a number to find its square root: "))
sqrt = math.sqrt(c)
rounded_num = round(sqrt,2) 
print("The square root of", c, "is", rounded_num)

d=int(input("Enter the number you want to be divided: "))
e=int(input("Enter the number you want to divide by: "))
division = math.fmod(d, e)
num_rounded = round(division, 2) 
print("The result of dividing", d, "by", e, "is", num_rounded)
