""" 
Task Manager
-------------------- 
a simple command_line app to keep track of  daily tasks.

Aurthur:[Emmanuel]
Date:[31/10/2025]
"""
import json
import os

def show_menu():
    """ Placeholder function for Menu """
    print("\n====== Task Manager======")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    """ Place holder function for data to be added to json file """
# receive user input
    title = input("Enter the title of the task: ").strip()
    due_date = input("Enter optional due date: ").strip()
    task = {"Title": title, "Due_date":due_date, "completed":False}
    # check if the json file already exists
    if os.path.exists("task.json") and os.path.getsize("task.json"):
        try:
        # Load existing file 
            with open("task.json", "r") as file:
                tasks = json.load(file)
                if not isinstance(tasks, list): 
                    # checks for a specific data type and return True/False value 
                    tasks = []
        except json.JSONDecodeError: # checks if the file is empty file / malformed json data
            tasks = []
    else:
        tasks = []  # start a fresh
    tasks.append(task)
    with open("task.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)
    print("Task added successfully")

def view_task():
    # open file in read mode
    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                tasks = []

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
        
    print("\n======= Your Tasks =======")
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks,1):
            status = "✓" if task.get("completed") else "✗"
            print(f"{i}. [{status}] {task['Title']} (Due: {task['Due_date']})")
    print("-" * 50)
    
def mark_task_done():
    try:
        with open("task.json", "r") as file: # open file in read mode
            tasks = json.load(file)
            if not isinstance(tasks, list): # check the data-type must be a list
                print("Error. File data invalid.Resetting to an empty list")
                tasks = [] # in the case the date-type isn't a list
            if not tasks:   # check for condition of an empty list
                print("No tasks were found. Please add tasks first ")
                return
            print("--------- Your list --------")
            for i, task in enumerate(tasks, 1): # loop through the json file
                status = "✓" if task.get("completed") else "✗"
                print(f"{i}. [{status}] {task['Title']} (Due:{task['Due_date']})")
            choice = input("\n Enter the number of the task you completed: ").strip()
            # check to user the value of choice is a number and within range
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(tasks): 
                print("Invalid choice. Please Enter a valid task number")
                return
                # This is to cover for the zero indexing in lists
            task_index = int(choice)  - 1
            tasks[task_index]["completed"] = True # change the status of uncompleted tasks
            print(f"Task: {tasks[task_index]['Title']} marked as completed!")
            # Re-open the file in write mode now
            with open("task.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print("All changes saved successfully")
    except FileNotFoundError:
        print("Error. No task file found. Please add task first")
    except json.JSONDecodeError:      # check for malformed file and empty file
        print("Error. File is corrupted. Please recreate the file")

def delete_task():
    """ Place holder function for tasks to be deleted """
    try:
        with open("task.json", "r") as new_file: # open file in read mode
            tasks = json.load(new_file)
            if not isinstance(tasks, list): # check the data-type must be a list
                print("Error. File data invalid.Resetting to an empty list")
                tasks = [] # in the case the date-type isn't a list
            if not tasks:   # check for condition of an empty list
                print("No tasks were found. Please add tasks first ")
                return
            for i, task in enumerate(tasks, 1): # loop through the json file
                status = "✓" if task.get("completed") else "✗"
                print(f"{i}. [{status}] {task['Title']} (Due:{task['Due_date']})")
            choice = input("\n Enter the number of the task you want to delete: ").strip()
            # check to user the value of choice is a number and within range
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(tasks): 
                print("Invalid choice. Please Enter a valid task number")
                return
                # This is to cover for the zero indexing in lists
            task_index = int(choice)  - 1
            delete_tasks = tasks.pop(task_index)
            print(f"Task, '{delete_tasks["Title"]}' was deleted successfully!")
            with open("task.json", "w") as new_file:
                json.dump(tasks, new_file, indent=4)
            print("All changes saved successfully")
    except FileNotFoundError:
        print("Error. No task file found. Please add task first")
    except json.JSONDecodeError:      # check for malformed file and empty file
        print("Error. File is corrupted. Please recreate the file")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice(1-5): ").strip()
        if choice == "1":
            print("Task added selected")
            add_task()
           # TODO implement call funtion
        elif choice == "2":
            print("View task selected")
            view_task()
        elif choice == "3":
            print("Mark as done selected")
            mark_task_done()
        elif choice == "4":
            print("Delete task selected")
            delete_task()
        elif choice == "5":
            print("Exiting.. goodbye!.")
            break
        else:
            print("Invalid input you entered out a value outside the range (1-5)")

if __name__ == "__main__":
    main()