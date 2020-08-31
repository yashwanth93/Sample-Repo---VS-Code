import math
import os
import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))
 
name = input("Your name mister? ")
print("Hello Mr.", name)

print("I am adding this print line to check how Git displays the 'diff' using clours red and green")
