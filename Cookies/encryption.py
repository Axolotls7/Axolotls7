# This is a little thing I made.
# Note: Don't use this in any software whose compromisation would spell doom for anyone. The code is litterally open to the public, and obscurity != security.
# Also, Stuart, if you read this (which I doubt you will), then hi! Does this look familiar?
# If you see this before I actually use it, then... uh... oops. Darn. Please don't tell people this is here, either way.
# Also, if you want me to remove your name, tell me! I will.
chart = {
    "A":{"a":"b","b":"c","c":"d","d":"f","e":"g","f":"h","g":"j"},
    "B":{"a":"k","b":"l","c":"m","d":"n","e":"p","f":"q","g":"r"},
    "C":{"a":"s","b":"t","c":"v","d":"w","e":"x","f":"y","g":"z"},
    "_":{"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"0"},
    "V":{"0":"a","1":"e","2":"i","3":"o","4":"u"}
}
def enc(plain):
    cipher = ""
    for word in plain.lower().split():
        for char in word:
            for first in chart:
                for second in chart[first]:
                    if chart[first][second] == char:
                        cipher += first + second
        cipher += " "
    return cipher.rstrip(" ")

def dec(cipher):
    plain = ""
    for word in cipher.split():
        for char in range(0, len(word), 2):
            first, second = word[char:char+2]
            plain += chart[first][second]
        plain += " "
    return plain.rstrip(" ")

while True:
    uin = input("What would you like to do?\n\t#1: Encode\n\t#2: Decode\n\t#3: Bug test: E->D\n\t#4: Bug test: D->E\n\t#0: Quit\n\t#")
    if int(uin) == 0:
        break
    match input("File or Text?\n\tNote: file will overwrite!\nf/t\n").lower():
        case "t":
            match int(uin):
                case 1:
                    print(enc(input()))
                case 2:
                    print(dec(input()))
                case 3:
                    print(dec(enc(input())))
                case 4:
                    print(enc(dec(input())))
                case _:
                    raise Exception("I don't know what that means.")
        case "f":
            f = input()
            text = open(f, "r").read()
            match int(uin):
                case 1:
                    open(f, "w").write(enc(text))
                case 2:
                    open(f, "w").write(dec(text))
                case 3:
                    open(f, "w").write(dec(enc(text)))
                case 4:
                    open(f, "w").write(enc(dec(text)))
                case _:
                    raise Exception("I don't know what that means.")