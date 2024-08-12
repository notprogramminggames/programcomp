import time
from games import *

cacl = "------------------------------------------------"


def texted():
    opt = int(
        input(
            "What would you like to do?\n---------------------------\n1: Add to the end of a file\n2: New file\n3: Letter Mode\n4: Read file\n5: Go back to previous menu\n---------------------------\n"
        )
    )
    if opt == 1:
        fn = input(
            "What is the file you would like to append to called? (Please make sure the file is in the same directory as the file for this program and you include the .txt at the end)\n"
        )
        time.sleep(0.5)
        subopt = input(
            "How would you like to append the text file?\n------------------------------------------------\n1: Carry on from where the file ends\n2: Start on a next line from where the file ends\n------------------------------------------------\n"
        )
        if subopt == "1":
            txtf = open(fn, "a")
            txt = input(
                "Now put what you want to put in that file:\n------------------------------------------\n"
            )
            txtf.write(txt)
            print("The file has now added onto with that text!")
            menu()
        elif subopt == "2":
            txtf = open(fn, "a")
            txtf.write("\n")
            txt = input(
                "Now put what you want to put in that file:\n------------------------------------------\n"
            )
            txtf.write(txt)
            print("The file has now added onto with that text!")
            time.sleep(0.5)
            menu()

    elif opt == 2:
        fntxt = input(
            "What would you like to name your file? (You need to put .txt or your preferred text file type at the end)\n"
        )
        # fntxt just means file name txt. Also i guess you could use this to write python, but you'd have to format it yourself in a better text editor.
        print(f"Your file has been named {fntxt}")
        txtf = open(fntxt, "w")
        txt = input(
            "Now put what you want to put in that file:\n------------------------------------------\n------------------------------------------\n"
        )
        txtf.write(txt)
        print("The file has now been written to!")
        menu()
    elif opt == 3:
        print(
            "This file will be seperate from the one on the other 2 options.\nAlso this is a WIP so things might be"
        )
        txtle = open("letter.txt", "w")
        name = input("Who is this letter addressed to?\n")
        ltxt = input(
            "Now put what you want to put in that letter:\n------------------------------------------\n------------------------------------------\n"
        )
        txtle.write("Dear ")
        txtle.write(name)
        txtle.write("\n\n")
        txtle = open("letter.txt", "a")
        txtle.write(ltxt)
        menu()
    elif opt == 5:
        print("\n")
        menu()
    elif opt == 4:
        optt = input(
            "What is the name of the file you would like to read? (Please include the file extension)\n"
        )
        txtf = open(optt, "r")
        print(txtf.readlines())
        menu()
    else:
        print("Sorry, but that option is invalid (text-ed)")


def calculator():
    num1 = float(input("What is your first number? "))
    oper = int(
        input(
            "Which operator would you like to use?\n1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)\n"
        )
    )
    num2 = float(input("What is your second number ? "))
    print(cacl)
    if oper == 1:
        print(num1 + num2)
    elif oper == 2:
        print(num1 - num2)
    elif oper == 3:
        print(num1 * num2)
    elif oper == 4:
        print(num1 / num2)
    else:
        print("Error")
    print(cacl)


def menu():
    print("Welcome to a compilation of some programs I made!")
    time.sleep(0.5)
    load = input(
        # This bit looks ugly but at least it looks nice when ran.
        "What would you like to load?\n----------------- \n|1:| Calculator  |\n|2:| Text editor |\n|3:| Games       |\n|4:| About       |\n-----------------\n"
    )
    if load == "1":
        calculator()
    elif load == "2":
        texted()
    elif load == "3":
        load2 = 1
        print(
            "This is a WIP, it's not done yet and is to be decided as to what it will be."
        )
        menu()
    elif load == "4":
        print(
            "this program was made by notprogramminggames and created on the 2nd of June 2024"
        )
    elif load == "exit":
        quit()
    else:
        print("The option number you entered was not valid.\n")
        menu()


menu()
