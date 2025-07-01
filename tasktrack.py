import json
from datetime import datetime
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist
    except json.JSONDecodeError:
        return [] 
    
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)    

def add_task():
    data=load_data()
    now = datetime.now().isoformat(timespec='seconds')
    tasks = input("enter your task to do: ")
    
    try:
        taskid = int(input("enter the priority number for this task: "))

        if any(task["taskid"] == taskid for task in data):
           raise ValueError("id already exists!")
        
    except ValueError:
          print("this priority already exists for a given task, see list to assign new id")
          taskid = int(input("enter the priority number for this task: "))
    
    try:
         status = input("enter your status for this task eg, todo, in progress, done: ").strip().lower()

         if status not in ["todo", "in progress", "done"]:
            raise ValueError("Invalid status")
            
    except ValueError:
       print("please enter a valid status as mentioned in eg")
       return
    try:
        tasks=str(tasks)
    except ValueError:
        print("invalid task, task type must be sentence")
        return
    
    data.append({"taskid":taskid, "tasks":tasks,"status":status, "created at" :now, "updated at":now})
    save_data(data)
    print(f"task {taskid} has been added successfully" )

def update_task():
    id = int(input("enter task id to be updated: "))
    data = load_data()
    now = datetime.now().isoformat(timespec='seconds')
    for task in data:
        if task["taskid"] == id:
           updatedtask = input("enter updated task: ")
           statusChange = input("update your task status eg todo, in progress, done").strip().lower()
           task["updated at"] = now
           task["tasks"] = updatedtask
           task["status"] = statusChange
           
           save_data(data)
           print(f"task {id} has been updated successfully" )
           return
    print("Task Id does not exist!")

def delete_task():
    id = int(input("enter your task id you wish to delete: "))
    data=load_data()
    for deltask in data:
        if deltask["taskid"] == id:
            data.remove(deltask)
            save_data(data)
            print("entry deleted successfully")
            return

    print("task id does not exist")

def list_task():
    print("these are all the tasks: ")
    data = load_data()
    if not data:
        print(" no tasks present yet ")
        return
    print("\n your tasks: ")
    for task in data:
        print(f" Task priority: {task['taskid']}, Tasks: {task['tasks']}")
def todo_tasks():
    data =load_data()
    for todotask in data:
        if todotask["status"] == "todo":
            print("Here are your tasks that are in progress\n")
            print( f" Task priority: {todotask['taskid']}, Tasks: {todotask['tasks']}, Status: {todotask['status']}")
            return
def done_tasks():
    data =load_data()
    for donetask in data:
        if donetask["status"] == "done":
            print("Here are your tasks that are done\n")
            print( f" Task priority: {donetask['taskid']}, Tasks: {donetask['tasks']}, Status: {donetask['status']}")
            return

def inprog_tasks():
    data =load_data()
    for inpro in data:
        if inpro["status"] == "in progress":
            print("Here are your tasks that are in progress\n")
            print(f" Task priority: {inpro['taskid']}, Tasks: {inpro['tasks']}, Status: {inpro['status']}")
            return
def main():
 
 while True: 
    print(" ")
    print("  ")
    print("welcome to your task tracker app\n")
    print("to add a task choose 1")
    print("to update a task choose 2")
    print("to delete a task choose 3")
    print("to list all tasks choose 4")
    print("to see todo  tasks choose 5")
    print("to see tasks in progress  choose 6")
    print("to see tasks that are done choose 7")
    print("to exit  choose 8\n")

    choice = int(input("please enter your choice: "))
    
    if choice == 1:
        add_task()
    elif choice == 2:
        update_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        list_task()
    elif choice == 5:
        todo_tasks()
    elif choice==6:
        inprog_tasks()
    elif choice ==7:
        done_tasks()
    elif choice == 8:
        print("Goodbye, thankyou for using")
        return
    else:
        print("invalid choice")

if __name__ == "__main__":
    main()
