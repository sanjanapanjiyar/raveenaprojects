print("Enter number to check if it is perfect")
num = int(input())
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors = sum_of_divisors + i
if sum_of_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")