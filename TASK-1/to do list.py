# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to list tasks
def list_tasks():
    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['task']} - [{status}]")

# Function to mark a task as complete
def mark_task_complete():
    list_tasks()
    task_number = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number!")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")