#This is a message-sending program
#It isn't good because it doesn't have a server and also some other things
#But if you really want to, you could do something with this
U = open("Users.txt", "w")
M = open("Messages.txt", "w")
peeps = dict((open("Users.txt", "r")).read())
messages = list((open("Messages.txt", "r")).read())
a = input("""Password
          
If new type new and trust the proccess""")
B = ""
if a == "new":
    a = input("Password")
    for i in range(0,len(a)):
        B = B + chr(ord(a[i])-2)
    User = input("Username")
    peeps.update(
        {B:User}
        )
    
else:
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
        print("""//quit
//see""")
    else:
        messages.append(User+": "+a)
U.write(str(messages))
M.write(str(peeps))