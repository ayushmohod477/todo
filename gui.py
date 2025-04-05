import function

import FreeSimpleGUI as sg

import time

sg.theme("black")


clock = sg.Text("", key="clock")
label = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My TO-DO App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 10), )

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %y %H:%M:%S"))
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo to Edit", font=("Helvetica", 10))

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values['todo']
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except ValueError:
                sg.popup("Please select a todo to Complete", font=("Helvetica", 10))

        case sg.WIN_CLOSED:
            break
        case "Exit":
            break


window.close()
