n=int(input("Enter a number to find out if it is prime or not: "))
def is_prime(num):
    prime = True
    if num <= 1:
        print(num,"is not a prime number")
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
         
         print(n,"is a prime number")
    else:
         print(n,"is not a prime number")
is_prime(n)