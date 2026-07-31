print("Enter number to check if it is positive and even or negative and even: ")
n=int(input("Enter number: "))
if n>0 and n%2==0:
    print("Number is positive and even")
elif n<0 and n%2==0:
    print("Number is negative and even")
else:
    print("Number is either odd or zero")