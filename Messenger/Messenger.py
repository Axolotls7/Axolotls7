#This is a message-sending program
#It isn't good because it doesn't have a server and also some other things
#But if you really want to, you could do something with this
#Obligatory copyright statement: Copyright (C) 2024 Rhys Forsberg, see COPYING.txt for license or type //license while logged in
import csv
import os
import traceback
from time import sleep
import random as rand
print("""© 2024 Axolotls7
    This program comes with ABSOLUTELY NO WARRANTY; for details type //warranty.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type //distribution for details.
    Type //license to see full license
    If you believe that I have made a mistake in choosing the displayed sections, please go to the GitHub repository Axolotls7/Axolotls7 and make an issue about it or start a pull request
    
    IMPORTANT: '//' commands only work while logged in""")
peeps = eval((open("Messenger/Users.txt", "r")).read())
with open("Messenger/messages.csv") as fp:
    messages = [row for row in csv.reader(fp, delimiter=",", quotechar='"')]

a = input("""

Menu
#0: Log in
#1: Sign up
#2: Guest
#3: quit

#""")
B = ""
if a == "1":
    a = input("Password, please: ")
    if a in peeps.keys():
        for i in range(0,len(a)):
            B = B + chr(ord(a[i])-2)
    User = input("Username, please: ").capitalize()
    try:
        userBox = open("Messenger/"+User+".csv","x+")
    except(OSError):
        print("Sorry, account names are first-come, first-serve, and somebody came before you. Restart the appplication")
        quit()
    peeps.update(
        {User:B}
    )
    
elif a == "0":
    a = input("Password, please: ")
    for i in range(0,len(a)):
        B = B + chr(ord(a[i])-2)
    User = input("Username: ").capitalize()
    try:
        assert B == peeps[User]
        print("Welcome,",User)
        userBox = open("Messenger/"+User+".csv")
    except:
        print("No.")
        quit()
    if User == "Admin":
        with open("Messenger/ALERTS.csv") as fp:
            ALERTS = [row for row in csv.reader(fp, delimiter=",", quotechar='"')]
        for i in range(0,len(ALERTS)):
            J = ""
            for j in ALERTS[i]:
                J = J + j
            print(J)
elif a == "2":
    User = "Guest"
elif a == "3":
    quit()
else:
    print("what?")
    quit()
print("type //help to see all commands")
mail = False


while True:
    try:
        a = input()
        if a == "":
            continue
        elif a == "//quit":
            break
        elif a == "//users":
            print(peeps.keys())
        elif a == "//sendmail":
            mail = True
            box = "Messenger/"+input("""Send mail to whom?
""").capitalize()+".csv"
            continue
        elif a == "//mail" and User != "Guest":
            print(userBox.read())
        elif a == "//see":
            for i in range(0,len(messages)):
                if type(messages[i]) == list:
                    J = ""
                    for j in messages[i]:
                        J = J + j
                    print(J)
                else:        
                    print(messages[i])
        elif a == "//license":
            print((open("COPYING.txt","r")).read)
        elif a == "//warranty":
            print("""15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.""")
        elif a == "//distribution":
            if input("It's really long. You sure?") == "yes":
                print("""
          4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.""")
        elif a == "//help":
            print("""
Basic
//quit: quit application
//help: shows this
Messages:
//see: shows all messages
//sendmail
//mail: show mailbox(WORK IN PROGRESS)
Licence:
//warranty: show GNU GPL 3.0 section 15
//distribution: show GNU GPL 3.0 section 16
//license: show full GNU GPL 3.0""")
        elif a == "//ADMIN":
            try:
                assert User == "Admin"
            except(AssertionError):
                for i in range(1,51):
                    try:
                        raise AttributeError("YOU ARE NOT ADMIN")
                    except(AttributeError):
                        print(traceback.format_exc())
                        try:
                            assert User == "Admin"
                        except:
                            print("YOU ARE NOT ADMIN")
                    try:
                        print("Y0U 4"+chr(rand.randint(-4,4)*i)+"3 N0"+chr(i-rand.randint(-20,20))+" 40"+chr(i)+"M1N")
                    except:
                        print("DIE DIE DIE DIE")
                    sleep(0.05)
                try:
                    raise AttributeError("YOU ARE NOT ADMIN")
                except(AttributeError):
                    print("DIE")
                    print(traceback.format_exc())
                print("  !!YOU ARE NOT ADMIN!!")
                print("""//YOU WILL BE REPORTED\\\\
\\\\YOU WILL BE REPORTED//""")
                with open("Messenger/ALERTS.csv", "a") as fp:
                    writer = csv.writer(fp, delimiter=",")
                    writer.writerows(["ALERT: "+User+" Tried to //ADMIN"])
                quit()
            do = input("""<Hello, Admin. What shall I do this time>
""").capitalize()
            if do == "Kill":
                do = input("""<Do I HAVE to?>
""").capitalize()
                if do == "Yes":
                    do = input("""<*sigh* Okay. Kill whom?>
""").capitalize()
                    if do == "Yourself" or do == "You":
                        print("*Facepalm* No.")
                        continue
                    elif do != ("nobody" or "Nobody"):
                        try:
                            del peeps[do]
                            os.remove("Messenger/"+do+".csv")
                        except(KeyError):
                            print("<who?>")
                            continue
                    else:
                        print("<Oh, phew. Bye!>")
                    continue
            elif do == "Show":
                print("<...>")
                do = input().capitalize()
                if do == "Computer?":
                    print("<...>")
                    sleep(1)
                    do = input("""<I don't wanna... it feels wrong.>
""").capitalize()
                    if do == "Please":
                        print("<Okay...>")
                        sleep(1)
                        print("<gimmie a sec>")
                        sleep(3)
                        do = input(peeps).capitalize()
                        if do == "Decrypt":
                            do = input("<NO! Do it yourself!>").capitalize()
                            if do == "Please?":
                                print("<No.>")
                                continue
        elif User != "Guest":
            if mail:
                with open(box, "a") as fp:
                    writer = csv.writer(fp, delimiter=",")
                    writer.writerows(a)
            else:
                messages.append(User+": "+a)
        elif User == "Guest":
            print("guest user cannot send messages. Please log in or sign up.")
        mail = False
    except(KeyboardInterrupt):
        a = input("""
Don't do that, it won't save!
""") 
        if a == "OVERRIDE":
            quit()


with open("Messenger/messages.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerows(messages)
with open("Messenger/Users.txt","w") as U:
    U.write(str(peeps))
