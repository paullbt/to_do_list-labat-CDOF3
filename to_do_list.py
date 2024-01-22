class Task:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTask Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks.append({"name": task_name, "completed": False})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index}. {task['name']} - {status}")

    def complete_task(self):
        self.view_tasks()
        task_index = int(input("Enter the task number to mark as complete: ")) - 1

        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        task_index = int(input("Enter the task number to delete: ")) - 1

        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

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
                print("Think You!!! Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 5.")


# Create an instance of the TaskManager and run the application
task_manager = Task()
task_manager.run()
