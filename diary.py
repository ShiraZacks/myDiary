import datetime

exit = False
counter = 0
while exit == False:
    print("Enter 'A' to create a new entry\n Enter 'B' to continue the current entry\n Enter 'E' to exit the application")
    userInput = input()

    if userInput == "A":
        counter +=1
        fileName = "Entry" + str(counter)
        file = open(fileName, "w")
        entry = input("Please write your entry:")
        file.write(str(datetime.datetime.now()) + "---------" + entry + "\n")
        file.close()

    if userInput == "B":
        file2 = open("Entry" + str(counter), "a")
        entry = input("Please write your addition:")
        file2.write(str(datetime.datetime.now()) + "---------" + entry + "\n")
        file2.close()
        
    if userInput == "E":
        exit = True