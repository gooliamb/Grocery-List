#To-Do List
#1/12/24
#Cristian and Julia

grocerylist= ["milk","chips","eggs","bananas"]



#Functions
def addtask():
    answ=input("What item would you like to add?:")
    grocerylist.insert(5,answ)
    Continue()

def completedtask():
    print(grocerylist)
    ans = input("Please enter an item to check off: ")
    i = grocerylist.index(ans)
    grocerylist[i] = ans + " " + "X"
    Continue()
    
def removetask():
    print ("Which item would you like to remove?: ")
    print (grocerylist)
    item=input("Item: ")
    if item == "milk":
        grocerylist.pop(0)
    elif item == "chips":
        grocerylist.pop(1)
    elif item == "eggs":
        grocerylist.pop(2)
    elif item == "bananas":
        grocerylist.pop(3)
    Continue()

def removeAll():
    grocerylist.clear()
    Continue()

def alphabetize():
    grocerylist.sort()
    print("Your list has been aphabetized")
    print (grocerylist)
    Continue()
    
def listAmount():
    print("The number of items on your list is:")
    print(len(grocerylist))
    Continue()

def Continue():
    ans=(input("Continue? Please type yes or no"))
    if ans == "yes":
        menu()
    if ans == "no":
        quit()

def menu():
    print ("Please choose an option: (Type in number between 1-5)")
    print ("1. Add a task to the To-Do List \n2. View the current To-Do List \n3. Mark a task as completed \n4. Remove a task from the To-Do list \n5. Remove all itemd from the list \n6. Sort the list alphabetically \n7. Print the # of items on the list \n8.Continue \n9. Exit The Program")
    option=int(input("Option:"))
    if option == 1:
        addtask()
    elif option == 2:
        print (grocerylist)
        menu()
    elif option == 3:
        completedtask()
    elif option == 4:
        removetask()
    elif option == 5:
        removeAll()
    elif option == 6:
        alphabetize()
    elif option == 7:
        listAmount()
    elif option == 8:
        menu()
    elif option == 9:
        quit()
    





#Main
menu()