class ToDo:
    HELP_MSG = {
        "add": "add a task to the to-do list",
        "complete": "mark a task as complete",
        "view all": "view the current tasks in the to-do list",
        "view complete": " view all the completed tasks in the to-do list",
        "view incomplete": "view all the uncompleted task",
        "help": "display all the help message",
        "delete": "delete the task",
        "exit": "exit the program",
        "restore": "restore the task from bin",
        "clear bin": "clears the bin",
        "view bin": "view bin",
    }

    def __init__(self):
        self.to_do = []
        self.bin = []

    def aid(self):
        for name, task in ToDo.HELP_MSG.items():
            print(name, task, sep="-->")

    def add_task(self, name, description):
        if any(task["task"] == name for task in self.to_do):
            print("Task already in the list")
        else:
            max_task_number = max((task["number"] for task in self.to_do), default=0)
            new_task = {
                "task": name,
                "description": description,
                "complete": False,
                "number": max_task_number + 1
            }
            print("Task added to the list")
            self.to_do.append(new_task)
            print(self.to_do)

    def task_complete(self, task_number):
        for task in self.to_do:
            if task["number"] == task_number:
                task["complete"] = True
                print(f"Task number {task_number} marked as complete")

    def display_to_do(self):
        for task in self.to_do:
            if task["complete"]:
                print(f"{task['task']} is complete")
            else:
                print(f"{task['task']} is incomplete")

    def all_complete_task(self):
        tasks = [task for task in self.to_do if task["complete"]]
        for task in tasks:
            print(f"{task['task']} complete")

    def incomplete_task(self):
        tasks = [task for task in self.to_do if not task["complete"]]
        for task in tasks:
            print(f"{task['task']} incomplete")

    def delete_task(self, task_id):
        task_found = False
        for task in self.to_do:
            if task['number'] == task_id:
                task_found = True
                confirm_delete = input("Do you want to delete permanently y/n?").lower()
                if confirm_delete == "y":
                    self.to_do.remove(task)
                    break
                else:
                    self.bin.append(task)
                    self.to_do.remove(task)
                    break
        if not task_found:
            print("invalid task id")

    def view_bin(self):
        if not self.bin:
            print("Bin is empty")
        else:
            for bin_item in self.bin:
                print(f'{bin_item["task"]} is in bin')

    def clear_bin(self):
        if not self.bin:
            print("Bin is empty")
        else:
            self.bin.clear()

    def restore_task(self):
        for bin_item in self.bin:
            self.to_do.append(bin_item)
        self.clear_bin()

todo = ToDo()
exit_confirm = False
todo.aid()
while not exit_confirm:
    user_command = input("What do you want to do: ").lower()
    print()
    if user_command == "add":
        task_name = input("Task Name: ")
        description = input("Task Description: ")
        todo.add_task(task_name, description)
    elif user_command == "complete":
        task_number = int(input("Task Number: "))
        todo.task_complete(task_number)
    elif user_command == "view all":
        todo.display_to_do()

    elif user_command == "view incomplete":
        todo.incomplete_task()
    elif user_command == "view complete":
        todo.all_complete_task()
    elif user_command == "help":
        todo.aid()
    elif user_command == "exit":
        exit_confirm = True
    elif user_command == "delete":
        task_id = int(input("Enter the task id"))
        todo.delete_task(task_id)
    elif user_command == "view bin":
        todo.view_bin()
    elif user_command == "clear bin":
        todo.clear_bin()
    elif user_command == "restore":
        todo.restore_task()
        print("Tasks restored from bin to to-do list")
    else:
        print("Wrong command")
        todo.aid()

