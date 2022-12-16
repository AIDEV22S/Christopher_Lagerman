import PySimpleGUI as sg


#Main Window
sg.theme('Topanga')
sg.set_options(text_color='white')
layout = [
    [sg.Button('Add Member',expand_x=True),sg.Button('Find Member'),sg.Button('Update Member',expand_x=True)],
    [sg.T('')],
    [sg.Button('Exit',expand_x=True)]
]

window = sg.Window('Membership Database',layout)

event, values = window.read()

def winRead():
    return window.read()

def getWindow():
    return window

#Add Member

add_layout = [[sg.T('First name:'), sg.Push(), sg.I(key='fnameInput')],
    [sg.T('Last name:') , sg.Push(), sg.I(key='lnameInput')],
    [sg.T('Adress:'),sg.Push(),sg.I(key='adressInput')],
    [sg.T('Post number:'),sg.Push(),sg.I(key='postnrInput')],
    [sg.T('Post adress:'),sg.Push(),sg.I(key='postaddrInput')],
    [sg.Button('Ok', expand_x=True), sg.Button('Clear')]
]

add_window = sg.Window('Add Member',add_layout)
def get_add_window():
    return add_window
