import function

import FreeSimpleGUI as sg

lable = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My TO-DO App",
                   layout=[[lable], [input_box, add_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
