print("Enter a year: ")
year=int(input("year: "))
if (year%4==0 or year%400==0 and not year%100==0):
    print("this year is a leap year")
else:
    print("this year is not a leap year")
