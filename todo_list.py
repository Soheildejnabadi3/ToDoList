def display_tasks(tasks):
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the task number to remove: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task removed.")
    else:
        print("Invalid task number.")

tasks = []
while True:
    print("\nOptions: 1. Add Task  2. Remove Task  3. View Tasks  4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        remove_task(tasks)
    elif choice == '3':
        display_tasks(tasks)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")