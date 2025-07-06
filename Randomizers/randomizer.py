import time
import json
import random
print("{<kch> //hello, this is your randomizer speaking|")
time.sleep(0.5)
print("//uh...|")
time.sleep(0.75)
print("//actually ɪᴅᴋ what I was going to say|\n")
while True:
    dir = input("//well, um... what ᴅɪʀᴇᴄᴛᴏʀʏ shall I load from_ [DIR(/)]}\n\t/").rstrip("/")
    file = input("{//okay, then which ғɪʟᴇ is it_ [FILE(.json)]}\n\t" + dir + "/").rstrip(".json")
    try:
        data = json.load(open(dir + "/" + file + ".json", "r"))
    except:
        match input("{<bzzt> //Well darn, that didn't work/\n//would you like to ᴛʀʏ ᴀɢᴀɪɴ_ [y/n]}\n\t"):
            case "y":
                continue
            case "n":
                break
            case _:
                print("{<bzzt> //I... y-... wha1110100101110101110101110_|/>}")
                break
    print(data[random.randInt(0,len(data)-1)])
