FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of todo items.
    :param filepath:
    :return:
    """
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the todo items list in the text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print('hello')
    print(get_todos())