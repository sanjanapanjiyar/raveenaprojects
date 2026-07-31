#Positional parameter
def printMessage(message):
    print(message)

def registerUser(userID, username, phone, city):
    print("User registered with the following details:")
    print("UserID:", userID)
    print("Username:", username)
    print("Phone:", phone)
    print("City:", city)



#functioncall
registerUser(1, "Raveena" , 6099178723, "New Jersey")

def loginName(nm = "Guest"):
    print("Logged in as:", nm)

#functioncall
loginName("Raveena")
loginName()


def loginName(username="Guest"):
    print("Logged in as:", username)

loginName("Raveena")
loginName()
#default parameter above

#Keyword parameter
registerUser(userID=1, username="Raveena", phone=6099178723, city="New Jersey")

#variable-length parameter
def total(*num):
    s = sum(num)
    print("Total:", s)

#function call
total(1, 2, 3, 4, 5)
total(10, 20, 30)

#variable length keyword parameter
def saveNumber(**args):
    print(args)

#function call
saveNumber(a=1, b=2, c=3)
