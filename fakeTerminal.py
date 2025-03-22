import sys
import curses

def run():
    while True:
        t = input()
        if t == "quit" and input("Are you sure? y/n") == "y":
            print("AxolOSl Terminal has closed.")
        elif t == "list programs":
            print("Programs:", "py (thon)", "pyos (py with tracebacks)", sep="\n\t")
        elif t == "run py":
            while True:
                t = input()
                if t == "#quit":
                    break
                print(">>>", end=" ")
                try:
                    eval(t)
                except:
                    return "PROCESS INTERRUPTED | AxolOSl has crashed."
        elif t == "run pyos":
            while True:
                t = input()
                if t == "#quit":
                    break
                eval(t)
print(run())
