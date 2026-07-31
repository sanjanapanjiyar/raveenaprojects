print("Enter a number for operation: 1 for cube, 2 for square")
num=int(input("Number: "))

num1=int(input("Numer for operation: "))
match num:
    case 1:
        if num1>0:
            print("Cube is ", num1*num1*num1)
    case 2:
        if num1>0:
            print("Square is ", num1*num1)

      
   
