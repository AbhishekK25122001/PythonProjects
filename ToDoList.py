#To do list

#List to store tasks
tasks=[]

#A function to let the user add a task
def add_task():
    task=input("Enter a new task: ")
    tasks.append({"task":task,"completed":False})
    print(f"Task'{task}' added!")

#Function to view all tasks
def view_tasks():
    if not tasks:
        print("No task found!")
    else:
        print("\nTo-Do List:")
        for i,task in enumerate(tasks,start=1):
            status="✔" if task["completed"] else "X"
            print(f"{i}.{task['task']} [{status}]")

#Function to mark a task as complete
def complete_task():
    view_tasks()
    try:
        task_num=int(input("\nEnter the task number to mark as complete: "))
        if 1 <=task_num <=len(tasks):
            tasks[task_num-1]["completed"]=True
            print(f"Task {task_num} marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num=int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <=len(tasks):
            removed_task = tasks.pop(task_num-1)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Menu function to display options and execute user choices
def menu():
    while True:
        print("\n------  To-Do List Menu -------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice=input("Choose an option (1-5): ")
        if choice =='1':
            add_task()
        elif choice =='2':
            view_tasks()
        elif choice=='3':
            complete_task()
        elif choice=='4':
            delete_task()
        elif choice=='5':
            print("GoodBye!")
            break
        else:
            print("Invalid choice. Please try again.")

#Run the program
menu()