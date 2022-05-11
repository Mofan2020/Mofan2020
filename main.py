#start
print("Hi! Welcome to MQ. This is a free app.")
print("start")
print("install python lib:sys time os numpy")
import sys
import os
import time
import math
print("loading MQ menu")
print("Finish!")
print("0.exit")
print("MQ type 1:1.multiplication 2.plus 3.low 4.same parts")
print("MQ type 2:5.count on fingers,stop on which fingers")
print("MQ MENU:  6.s=? 7.pi=?")
while True:
    # noinspection SpellCheckingInspection
    inpt = int(input("MQ:"))
    if inpt == 1:
        a = int(input("number1:"))
        b = int(input("number2:"))
        c = a * b
        print("is:", c)
        time.sleep(2)
    elif inpt == 2:
        a = int(input("number1:"))
        b = int(input("number2:"))
        c = a + b
        print("is:", c)
        time.sleep(2)
    elif inpt == 3:
        a = int(input("number1:"))
        b = int(input("number2:"))
        c = a - b
        print("is:", c)
        time.sleep(2)
    elif inpt == 4:
        a = int(input("number1:"))
        b = int(input("number2:"))
        c = a / b
        print("is:", c)
        time.sleep(2)
    elif inpt == 5:
        print("404 not fount")
        time.sleep(1)
    elif inpt == 6:
        a = int(input("number1:"))
        b = int(input("number2:"))
        c = a * b
        print("S:", c)
        time.sleep(2)
    elif inpt == 7:
        c = math.pi
        print("pi:", c)
    elif inpt == 0:
        print("exit")
        time.sleep(1)
        sys.exit(0)
