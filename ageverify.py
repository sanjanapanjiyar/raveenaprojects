print("Enter your age: ")
age=int(input("age:"))
if age<18 and age>=0:
    print("Minor")
elif age>=18 and age<65:
    print("Major")
elif age>=65:
    print("Senior citizen")
else:
    print("Wrong age")
