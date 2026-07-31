print("Enter 2 values")
a=int(input("First value: "))
b=int(input("Second value: "))
print("Enter + for addition - for subtraction")
opr=input("Operator: ")
match opr:
    case "+":
        print("Addition is " , (a + b))
    case "-":
        print("Subtraction is " , (a - b))
    case _:
        print("Invalid operator")

# same operation using if:

if opr == "+":
    print("Addition is " , (a + b))
elif opr == "-":
    print("Subtraction is " , (a - b))
else:
    print("Invalid operator")
