operation=input("Enter operation symbol ")
if operation=="+":
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    result=a+b
    print("Addition is", result)
elif operation=="-":
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    result=a-b
    print("Subtraction is", result)
elif operation=="*":
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    result=a*b
    print("Multiplication is", result)
elif operation=="/":
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    result=a/b
    print("Division is", result)
else:
    print("Invalid operation symbol")
