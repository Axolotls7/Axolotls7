#This is a message-sending program
#It isn't good because it doesn't have a server and also some other things
#But if you really want to, you could do something with this
peeps = {}
messages = []
a = input("""Password

If new type new and trust the proccess""")
if a == "new":
    peeps.update({input(Password):input(Username)})
else:
    try:
        print(peeps[a])
    except(keyError):
        quit()
