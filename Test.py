import PySimpleGUI as sg

# design 1: "one-shot"/lukker ved ineregering

# definerer layout
layout = [
    [sg.Text("Hvad hedder du?")],
    [sg.Input()],
    [sg.Button("Ok"), sg.Button("Luk")],
    ]

# opretter vindue
window = sg.Window("Test", layout)

# interegering med vindue
event, values = window.read()

window.close()

# evt. pop-up med info
sg.popup("Hej", values[0])

"""
# design 2: loop/lukker ikke ved interegering

# definerer layout
layout = [
    [sg.Text("Hvad hedder du?")],
    [sg.Input()],
    [sg.Button("Ok"), sg.Button("Luk")],
    ]

# opretter vindue
window = sg.Window("Test", layout)

# event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Luk":
        break
    if event == "Ok":
        print("Hej", values[0])

window.close()
"""