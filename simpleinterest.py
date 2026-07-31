amount=50000
time=36
rate=5
simple_interest=(amount*time*rate)/100
print("Simple Interest is" , simple_interest)

phy=float(input("Enter the physics marks: "))
chem=float(input("Enter the chemistry marks: "))
math=float(input("Enter the mathematics marks: "))
total=phy+chem+math
per=total/3
print("Average percentage is" , per)
print("Data type of physics is " , type(phy))
print("Data type of chemistry is " , type(chem))
print("Data type of mathematics is " , type(math))

# input() to accept values from user
# eg, a=int(input("Enter number: "))