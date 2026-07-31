counter=0
while counter>0:
    print(counter)
    counter=counter-2

n=int(input("Enter a number: "))
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    print("Last digit = ", r)
    n=int(n/10)
print("Reversed number = ", rev)