class TaskManager:
    def __init__(self):
        self.tasks = []

    def menu(self):
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. View Completed Tasks")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

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

    def view_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task["completed"]]
        if not completed_tasks:
            print("No completed tasks available.")
        else:
            print("\nCompleted Tasks:")
            for index, task in enumerate(completed_tasks, start=1):
                print(f"{index}. {task['name']} - Completed")

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
            self.menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_completed_tasks()
            elif choice == "4":
                self.complete_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Thank You!!! Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 6.")


# Create an instance of the TaskManager and run the application
task_manager = TaskManager()
task_manager.run()
