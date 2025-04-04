def get_todos(filepath):
    """Read a file and return a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """To write in a file"""
    with open(filepath, 'w') as file_arg:
        file_arg.writelines(todos_arg)
        file_arg.close()
