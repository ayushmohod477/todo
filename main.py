from function import get_todos, write_todos
import time
now = time.strftime("%b %d, %y %H:%M:%S")
print("it is now,", now)
print("something")
while True:
    user_action = input("Type add,show, edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos('todos.txt')

        todos.append(todo + "\n")

        write_todos('todos.txt', todos)

    elif user_action.startswith("show"):

        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos('todos.txt')

            new_todo = input("Enter a new todoo:")
            todos[number] = new_todo + "\n"

            write_todos('todos.txt', todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = get_todos('todos.txt')

            completed_todo = todos[number].strip('\n')

            todos.pop(number)

            write_todos('todos.txt', todos)

            message = f"congrats {completed_todo} is completed 🎉"
            print(message)

        except IndexError:
            print("there is no todo with such number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid")

print("bye")
