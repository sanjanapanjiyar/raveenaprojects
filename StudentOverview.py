print("Student Details")
name=input("Enter student name: ")
roll=input("Enter student roll number: ")
physics=float(input("Enter student physics marks: "))
chemistry=float(input("Enter student chemistry marks: "))
maths=float(input("Enter student maths marks: "))
compsci=float(input("Enter student computer science marks: "))

percentage=(physics+chemistry+maths+compsci)/4

if percentage>=75:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="C"
else:
    grade="Fail"

print("Enter A to view marksheet, B to view grade, and C to view percentage: ")
choice=input("Enter operation choice: ")

match choice:
    case "A":
        print(roll, name, physics, chemistry, maths, compsci, percentage, grade)
    case "B":
        print("Grade is:", grade)
    case "C":
        print("Percentage is:", percentage)
    case "_":
        print("Wrong choice")

