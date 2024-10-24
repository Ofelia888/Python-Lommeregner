import PySimpleGUI as sg

layout = [
    [sg.Input(size=(15,3), key = "input1_display")],
    [sg.Input(size=(15,3), key = "input2_display")],
    [sg.Button("+", key = "addition_operator"), sg.Button("-", key = "subtraction_operator"), sg.Button("*", key = "multiplication_operator"), sg.Button("/", key = "division_operator")],
    [sg.Text(0, font=(50), key = "result_display")]
]

window = sg.Window("Calculator", layout)

# calculator functions
def update_display(display_value):
    if event in "addition_operator" or event in "subtraction_operator" or event in "multiplication_operator" or event in "division_operator":
        window["result_display"].update(display_value)

while True:
    event, values = window.read()
    if event is None:
        break

    input1 = float(layout[0][0].get())
    input2 = float(layout[1][0].get())

    if event in "addition_operator":
        result = input1 + input2
        update_display(result)
    elif event in "subtraction_operator":
        result = input1 - input2
        update_display(result)
    elif event in "multiplication_operator":
        result = input1 * input2
        update_display(result)
    elif event in "division_operator":
        result = input1 / input2
        update_display(result)
    if event == sg.WINDOW_CLOSED:
        break