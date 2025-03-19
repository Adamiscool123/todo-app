def get_todos(filepath='todos.txt'):
    """Read a text file and return the list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def get_now(todos_arg, filepath='todos.txt'):
    """Write a to-do items list in the text file."""
    with open(filepath, "w") as file:
        stop_local = file.writelines(todos_arg)
    return stop_local


