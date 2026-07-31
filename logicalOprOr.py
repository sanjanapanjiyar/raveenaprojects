str=input("Enter operation: ")
n=int(input("Enter first number: "))
n1=int(input("Enter second number: "))

print("Enter 'add' to perform addition")
if(str=="add" or str=="ADD"):
    print("Result:", n+n1)
print("Enter 'sub' to perform subtraction")
if(str=="sub" or str=="SUB"):
    print("Result:", n-n1)  
print("Enter 'mul' to perform multiplication")
if(str=="mul" or str=="MUL"):
    print("Result:", n*n1)
print("Enter 'div' to perform division")
if(str=="div" or str=="DIV"):
    if n1!=0:
        print("Result:", n/n1)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")
