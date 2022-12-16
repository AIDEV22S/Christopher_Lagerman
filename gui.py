import PySimpleGUI as sg

sg.theme('Topanga')
sg.set_options(text_color='black')
layout = [
    [sg.T('id'),sg.Push(), sg.I(key='idInput')],
    [sg.T('Name'),sg.Push(),sg.I(key='nameInput')],
    [sg.Button('OK',expand_x=True),sg.Button('Clear'),sg.Button('Exit',expand_x=True)]
]

window = sg.Window('Test',layout)

event, values = window.read()

def winRead():
    return window.read()

def getWindow():
    return window

def clear_UI():
    for key in values:
        window['idInput'].update('')
        window['nameInput'].update('')
        return None

def ok_pressed(arg1):
    for key in values:
        window['idInput'].update(arg1)
        return None
