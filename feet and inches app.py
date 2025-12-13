import FreeSimpleGUI as sg
from converters import convert

sg.theme("Black")

label1 = sg.Text("Enter feet")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Converter", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button,exit_button, output_label]])


while True:
    event, values = window.read(timeout=200)
    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            meters = convert(feet, inches)
            window["output"].update(value=f"{meters}m")
        case "Exit":
            break

window.close()