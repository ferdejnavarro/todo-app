# from functions import get_todos, write_todos

import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):

        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            print('Here you have the existing todos', todos)

            new_todo = input("Enter the new todo ")
            todos[number] = new_todo + '\n'

            print('Here is the new todo list', todos)

            functions.write_todos(todos, 'todos.txt')

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos, 'todos.txt')

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command.")

print("Bye!")
