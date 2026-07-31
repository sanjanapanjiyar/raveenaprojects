n1=int(input("Enter value for n1: "))
n2=int(input("Enter value for n2: "))
n=int(input("Enter value for n: "))

if(n>n1):
    if(n>n2):
        print("n is greater than both n1 and n2")
    else:
        print("n is greater than n1 but not n2")
elif(n1>n2):
    print(f"n ({n}) is not greater than n1 ({n1}) but n1 ({n1}) is greater than n2 ({n2})")
else:
    print(f"n ({n}) is not greater than n1 ({n1}) and n1 ({n1}) is not greater than n2 ({n2})")
    print(f"n ({n}) is not greater than n1 ({n1})")

# change text to variables later to show the actual values of n, n1, and n2