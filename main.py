import PySimpleGUI as sg
import pyperclip as pc

layout = [
    [sg.Text("Enter text:")],
    [sg.Input(key="text_input")],
    [sg.Multiline(key="text_output")],
    [sg.Button("Copy", key="submit")]
]

window = sg.Window("Discord Region Indicator emoji tool", layout)

def reg_indicator_convert(char):
    output = ":regional_indicator_" + char + ":"
    return output

prev_input = ""
output_string = ""

while True:
    event, values = window.read(timeout=250)
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event != '__TIMEOUT__':
        print(event, values)

    if values["text_input"] != prev_input:
        output_string = ""
        for char in values["text_input"].lower():
            if char != " ":
                output_string = output_string + reg_indicator_convert(char) + " "
            else:
                output_string = output_string + " "
        window["text_output"].update(output_string)

    if event == "submit":
        pc.copy(output_string)

