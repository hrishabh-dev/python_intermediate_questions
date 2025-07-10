print("simple task manager ")

list=[]
def addtask(): 
    a=input("Enter task:-")
    list.append(a)
    print("-------------------------")

def showtask():
    if not list:
        print("No tasks are saved")
    else :
        print("Tasks.")
        for idx,tasks in enumerate(list,1):
            print(f"{idx}:-{tasks}")
        print("-------------------------")
def deletetask():
    if not list:
        print("No task is available to delete")
        print("----------------------------")
        return
    showtask() 
    try:
        x=int(input("enter the no of task to delete:-"))
        if 1<=x<=len(list):
            rmtask=list.pop(x-1)
            print(f"Deleted task is {x} : {rmtask}")
        else:
            print('invalid number')
    except ValueError:
        print("Please enter a valid number")


check=True

while check: 
    print("1. add task")
    print("2. Show task")
    print("3. Delete task")
    print("4. Exit")
    a=int(input("Enter value :-"))
    print("--------------------------")
    if a==1:
        addtask()
    elif a==2:
        showtask()
    elif a==3:
        deletetask()
    elif a==4:
        check=False
        print("Exiting...")
        print("Thank you please visit again")
        break
    else:
        print("Invalid input please try again")


