import json
from pathlib import Path

FILE = Path("tasks.json")


def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []


def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2))


tasks = load_tasks()

while True:
    print("\n=== Student Study Planner ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['name']} - {status}")

    elif choice == "2":
        name = input("Enter task: ").strip()
        if name:
            tasks.append({"name": name, "done": False})
            save_tasks(tasks)
            print("Task added!")

    elif choice == "3":
        try:
            number = int(input("Task number: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                save_tasks(tasks)
                print("Task completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

    elif choice == "4":
        print("Good luck with your studies!")
        break

    else:
        print("Choose an option from 1 to 4.")
