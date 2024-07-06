import time

cacl = "------------------------------------------------"
# cacl just means calculato line


def texted():
    opt = input(
        "What would you like to do?\n1: Add to the end of a file\n2: New file\n3: Letter Mode\n4: Read file\n5: Go back to previous menu\n"
    )
    if opt == "1":
        fn = input(
            "What is the file you would like to add on to called? (Please make sure the file is in the same directory as the file for this program and you include the .txt at the end)\n"
        )
        txtf = open(fn, "a")
        txt = input(
            "Now put what you want to put in that file:\n------------------------------------------\n"
        )
        txtf = open("your file.txt", "a")
        txtf.write(txt)
        print("The file has now added onto with that text!")
    if opt == "2":
        fntxt = input(
            "What would you like to name your file? (You need to put .txt or your preferred text file type at the end)\n"
        )
        # fntxt just means file name txt
        print("This file will be a .txt file, you can change this later.\n")
        txtf = open(fntxt, "w")
        txt = input(
            "Now put what you want to put in that file:\n------------------------------------------\n------------------------------------------\n"
        )
        txtf.write(txt)
        print("The file has now been written to!")
    if opt == "3":
        print(
            "This file will be seperate from the one on the other 2 options.\nAlso this is a WIP so things might be"
        )
        txtle = open("letter.txt", "w")
        ad = input("Who is this letter addressed to? ")
        ltxt = input(
            "Now put what you want to put in that letter:\n------------------------------------------\n------------------------------------------\n"
        )
        txtle.write(ad)
        txtle = open("letter.txt", "a")
        txtle.write(ltxt)
    if opt == "5":
        print("\n")
        menu()
    if opt == "4":
        optt = input(
            "Would you like to read 'your file.txt' (1),'letter.txt' (2) or 'sample.txt' (3)"
        )


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
        "What would you like to load?\n----------------- \n|1:| Calculator  |\n|2:| Text editor |\n|3:| Games       |\n|4:| About       |\n|5:| Changelog   |\n-----------------\n"
    )
    if load == "1":
        calculator()
    if load == "2":
        texted()
    if load == "3":
        load2 = 1
        print(
            "This is a WIP, it's not done yet and is to be decided as to what it will be."
        )
        menu()
    if load == "4":
        print("this program was made by notprogramminggames")
    if load == "5":
        print(
            "Changelog:\n 2nd June 2024: Program created\n 23rd June 2024: I think calculator was added this day\n Some stuff happened but I dont remember when\n 6th July 2024: Text editor improved so that files could be named instead of being called 'your file.txt'\n Letter mode also added to text editor"
        )


menu()
