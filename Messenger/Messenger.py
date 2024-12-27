#This is a message-sending program
#It isn't good because it doesn't have a server and also some other things
#But if you really want to, you could do something with this
U = open("Users.txt", "w")
M = open("Messages.txt", "w")
peeps = dict(read(open("Users.txt")))
messages = list(read(open("Messages.txt")))
a = input("""Password

If new type new and trust the proccess""")
if a == "new":
    peeps.update(
        {chr(ord(input(Password))-2):input(Username)})
else:
    try:
        print(peeps[chr(ord(a)-2)])
    except(keyError):
        quit()
while True:
    a = input()
    if a == "//quit":
        break
    else messages.append(a)
U.write(messages)
M.write(peeps)
