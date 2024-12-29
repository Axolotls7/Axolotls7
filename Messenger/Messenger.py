#This is a message-sending program
#It isn't good because it doesn't have a server and also some other things
#But if you really want to, you could do something with this
U = open("Users.txt", "w")
M = open("Messages.txt", "w")
peeps = dict((open("Users.txt", "r")).read())
messages = list((open("Messages.txt", "r")).read())
a = input("""

Menu
#0: Enter password
#1: New account
#2: quit
#""")
B = ""
if a == "1":
    a = input("Password, please: ")
    for i in range(0,len(a)):
        B = B + chr(ord(a[i])-2)
    User = input("Username, please: ")
    peeps.update(
        {B:User}
        )
    
elif a == "0":
    a = input("Password, please: ")
    for i in range(0,len(a)):
        B = B + chr(ord(a[i])-2)
    try:
        User = peeps[B]
        print()
    except(KeyError):
        quit()
print("type //help to see all commands")
while True:
    a = input()
    if a == "//quit":
        break
    elif a == "//see":
        for i in range(0,len(messages)):
            print(messages[i])
    elif a == "//help":
        print("""
Commands
//quit____
//see: shows all messages
//mail""")
    else:
        messages.append(User+": "+a)
U.write(str(messages))
M.write(str(peeps))
