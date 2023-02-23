import os

while 1:
    entry = int(
        input(
            """
        
        Please enter your action
        Press 1 to take new note
        Press 2 to view already created note
        Press 3 to add new note to already existed note
        Press 4 to return to main menu
        
        ---->>"""
        )
    )

    if entry == 1:
        f = open("notes.txt", "w")
        os.system("cls")
        txt = input("Start making your notes\n\n")
        f.write(txt)
        f.close()

    elif entry == 2:
        f = open("notes.txt", "r")
        ch = f.readlines()
        for x in ch:
            print(x, end="")
        f.close()

    elif entry == 3:
        f = open("notes.txt", "r+")
        ch = f.readlines()
        for x in ch:
            print(x, end="")
        txt = input()
        f.write(txt)
        f.close()

    elif entry == 4:
        break
    
    else:
        print("Enter a valid input")
