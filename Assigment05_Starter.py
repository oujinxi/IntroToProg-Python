# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jin Ou, 11.06.2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
lstRow = []  # row of txt data turn into list
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
objFile = open(objFile,"r")
for strData in objFile:
    lstRow = strData.split(",")
    dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for lstRow in lstTable:
            print(lstRow['Task']+","+lstRow['Priority'])

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask=input("Enter the Task: ")
        strPriority=input("Enter the Priority: ")
        dicRow = {"Task":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        print("New Item Added.")

        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        delTask = input("Enter the Task you Wish to Delete: ")
        for lstRow in range(len(lstTable)):
            if lstTable[lstRow]['Task'] == delTask:
                del lstTable[lstRow]
                print("Removed.")
            else:
                print("Item Doesn't exist.")
        #for lstRow in lstTable:
        #    if delTask in lstRow:
        #        lstTable.remove(lstRow)
        #        print("Removed.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")

        for objRow in lstTable:
            objFile.write(objRow['Task']+","+objRow['Priority']+"\n")
        objFile.close()
        print("Data Saved.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
