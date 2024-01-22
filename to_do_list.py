from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class TaskManager:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n=== " + Fore.CYAN + "Task Manager" + Style.RESET_ALL + " ===")
        print("1. " + Fore.GREEN + "Add Task" + Style.RESET_ALL)
        print("2. " + Fore.YELLOW + "View Tasks" + Style.RESET_ALL)
        print("3. " + Fore.BLUE + "Mark Task as Complete" + Style.RESET_ALL)
        print("4. " + Fore.MAGENTA + "Delete Task" + Style.RESET_ALL)
        print("5. " + Fore.RED + "Exit" + Style.RESET_ALL)

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks.append({"name": task_name, "completed": False})
        print(Fore.GREEN + f"Task '{task_name}' added successfully!" + Style.RESET_ALL)

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks available." + Style.RESET_ALL)
        else:
            print("\n" + Fore.YELLOW + "Tasks:" + Style.RESET_ALL)
            for index, task in enumerate(self.tasks, start=1):
                status = Fore.GREEN + "Completed" + Style.RESET_ALL if task["completed"] else Fore.RED + "Not Completed" + Style.RESET_ALL
                print(f"{index}. {task['name']} - {status}")

    def complete_task(self):
        self.view_tasks()
        if not self.tasks:
            print(Fore.YELLOW + "No tasks available." + Style.RESET_ALL)
            return

        task_index = int(input("Enter the task number to mark as complete: ")) - 1

        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(Fore.BLUE + "Task marked as complete!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number." + Style.RESET_ALL)

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            print(Fore.YELLOW + "No tasks available." + Style.RESET_ALL)
            return

        task_index = int(input("Enter the task number to delete: ")) - 1

        if 0 <= task_index < len(self.tasks):
            deleted_task_name = self.tasks[task_index]["name"]
            del self.tasks[task_index]
            print(Fore.MAGENTA + f"Task '{deleted_task_name}' deleted successfully!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number." + Style.RESET_ALL)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print(Fore.RED + "Thank you! Goodbye!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5." + Style.RESET_ALL)

# Create an instance of the TaskManager and run the application
task_manager = TaskManager()
task_manager.run()

