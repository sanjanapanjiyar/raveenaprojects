print("Enter number to check if it is prime")
num = int(input())

match num:
    case 1:
        print("Not prime")
    case _:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print("Not prime")
            else:
                print("Prime")
        else:
            print("Not prime")


