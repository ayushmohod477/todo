import function

import FreeSimpleGUI as sg

lable = sg.Text("Type in a TO-DO")
input_box = sg.InputText(tooltip="enter todo")
add_button = sg.Button("ADD")

window = sg.Window("My TO-DO App", layout=[[lable], [input_box, add_button]])
window.read()
window.close()
