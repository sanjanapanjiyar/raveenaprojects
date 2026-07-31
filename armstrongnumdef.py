n=int(input("Enter a number to check if it is an Armstrong number: "))

def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    if sum_of_powers == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

is_armstrong(n)
