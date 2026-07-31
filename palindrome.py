n=int(input("Enter a number to see if it is a palindrome: "))
original_n = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
if original_n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")