from functions import get_todos, get_now
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo+"\n")
        get_now(todos, 'todos.txt')

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            updated = f"{index+1}.{item.title()}"
            print(updated)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            get_now(todos, 'todos.txt')
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            comp = int(user_action[9:])
            todos = get_todos()
            number = comp - 1
            todo_removed = todos[number]
            todos.pop(number)
            get_now(todos, 'todos.txt')
            message = f"Todo: {todo_removed.title()}was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number try again")
            continue

    elif "exit" in user_action:
        break

    else:
        print("This Command is not valid")
        number = int(user_action[5:])
        number = number - 1
print("Bye")


