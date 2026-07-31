n=int(input("Enter a number to check if it is odd or even: "))
def is_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

is_odd(n)
