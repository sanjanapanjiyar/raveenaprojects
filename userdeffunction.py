def displayMessage():
    print("Hello all")

displayMessage() # 1st function call
displayMessage() # 2nd function call
displayMessage() # 3rd function call

def factor(num):
    for n in range(1,num-1):
        if (num % n == 0):
            print (n)
factor(12) # function call