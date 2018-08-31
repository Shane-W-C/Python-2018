import random
import time
import sys

name = " "

while True:
    if name == " ":
        print("Please type your name:")
        name = input()
        if name != " ":
            print("Thank you for personalizing this, %s." % name)
    break

answers = ["Not going to happen, %s." % name, "Please, try asking again.", "It is extremely likely.", "%s, I'm gonna be straight with you, not happening." % name, "How should I know?", "I believe that your chances are great, %s." % name]

time.sleep(1)

print("Welcome to Magic 8-Bit.")

print(" .-'''-.")
print("/   v   \\")
print("|  (8)  |")
print("\   ^   /")
print(" '-...-'")

print("Please, ask me a question, or say [N]o to leave:")

while True:
    cmd = input()
    if cmd.strip()!= "n" and cmd.lower() != "n":
        time.sleep(1)
        print(random.choice(answers))
        time.sleep(1)
        print( "Ask another question, or press [N] to leave.")

    else:
        break
print("Have a nice day.")

sys.exit()


