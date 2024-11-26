# To-Do List Application

# Initialize an empty to-do list
todo_list = []

def display_menu():
    """Displays the menu options."""
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks():
    """Displays all tasks."""
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{index}. {task['description']} {status}")

def add_task():
    """Adds a new task to the list."""
    task = input("\nEnter the task description: ")
    todo_list.append({"description": task, "completed": False})
    print(f"Task '{task}' added!")

def remove_task():
    """Removes a task from the list."""
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['description']}' removed!")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

def mark_completed():
    """Marks a task as completed."""
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        todo_list[task_number - 1]['completed'] = True
        print(f"Task '{todo_list[task_number - 1]['description']}' marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
