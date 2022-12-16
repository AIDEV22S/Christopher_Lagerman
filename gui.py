import PySimpleGUI as sg


#Main Window
sg.theme('Topanga')
sg.set_options(text_color='white')
layout = [
    [sg.Button('Add Member',expand_x=True),sg.Button('Find Member'),sg.Button('Update Member',expand_x=True)],
    [sg.Text(' ')],
    [sg.T('Chose an action.',key='msg',justification='center')],
    [sg.Button('Exit',expand_x=True)]
]

window = sg.Window('Membership Database',layout)

event, values = window.read()

def winRead():
    return window.read()

def getWindow():
    return window

def update_msg(msg):
    window['msg'].update(msg)
#Add Member
def get_addLayout():
    return [[sg.T('First name:'), sg.Push(), sg.I(key='fnameInput')],
    [sg.T('Last name:') , sg.Push(), sg.I(key='lnameInput')],
    [sg.T('Adress:'),sg.Push(),sg.I(key='adressInput')],
    [sg.T('Post number:'),sg.Push(),sg.I(key='pnrInput')],
    [sg.T('Post adress:'),sg.Push(),sg.I(key='padrInput')],
    [sg.Button('OK', expand_x=True), sg.Button('Clear')]
]

#Find Member
def get_findLayout():
            return [
            [sg.T('Type the ID of:'),sg.I('',key='fID')],
            [sg.T('Result: ', key='fResult')],
            [sg.Button('Search',expand_x=True)]
            ]
def make_findWindow(layout):
    sg.Window('Find Member',layout)