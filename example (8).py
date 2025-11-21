# Created on iPad.
todo = []

def new():
    add = input("add new todo list: ")
    todo.append(add)

def mrt():
    remove = input("remove to do list: ")
    todo.remove(remove)

def tyu():
    todo.clear()   

def front():
    print("welcome")
    print("Your To do list")
    print("please press 1 to add to do list")
    print("please press 2 to remove to do list")
    print("please press 3 to change to do list")
    c = input("choose :")
    if c == "1":
        new()            
    elif c == "2":
        mrt()           
    elif c == "3":
        tyu()           
    else:
        print("Invalid result")

while True:              
    front()
