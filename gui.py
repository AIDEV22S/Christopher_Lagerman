import PySimpleGUI as sg

# Main Window
sg.theme('Topanga')
sg.set_options(text_color='white')

layout = [
    [sg.Button('Add Member', expand_x=True), sg.Button('Find Member', expand_x=True)],
    [sg.Text(' ')],
    [sg.T('Chose an action.', key='msg', justification='center')],
    [sg.Button('Exit', expand_x=True)]
]

window = sg.Window('Membership Database', layout)

event, values = window.read()


def winRead():
    return window.read()


def getWindow():
    return window


def update_msg(msg):
    window['msg'].update(msg)
    return None


# Add Member
def get_addLayout():
    return [[sg.T('First name:'), sg.Push(), sg.I(key='fnameInput')],
            [sg.T('Last name:'), sg.Push(), sg.I(key='lnameInput')],
            [sg.T('Adress:'), sg.Push(), sg.I(key='adressInput')],
            [sg.T('Post number:'), sg.Push(), sg.I(key='pnrInput')],
            [sg.T('Post adress:'), sg.Push(), sg.I(key='padrInput')],
            [sg.Button('OK', expand_x=True), sg.Button('Clear')]
            ]

def clear_add(window):
    window['fnameInput'].update('')
    window['lnameInput'].update('')
    window['adressInput'].update('')
    window['pnrInput'].update('')
    window['padrInput'].update('')


# Find Member
def get_findLayout():
    return [
        [sg.T('Type member ID:'), sg.I('', key='fID')],
        [sg.T('')],
        [sg.Button('Search', expand_x=True)]
    ]


def make_findWindow(layout):
    sg.Window('Find Member', layout)
    return None


# Update Member

def get_updateLayout(memb):
    return [[sg.T('Name:'), sg.T(f'{memb.get_name()}', key='mName')],
            [sg.T('Adress:'), sg.T(f'{memb.get_adr()}', key='mAdr')],
            [sg.T('Post Adress:'), sg.T(f'{memb.get_post()}', key='mPadr')],
            [sg.T('Paid Membership:'), sg.T(f'{memb.get_paid()}', key='mPaid')],
            [sg.Button('Toggle Paid Membership', expand_x=True),sg.Button('Delete Member',expand_x=True)]
            ]

def updateInfo(window,memb):
    window['mName'].update(memb.get_name())
    window['mAdr'].update(memb.get_adr())
    window['mPadr'].update(memb.get_post())
    window['mPaid'].update(memb.get_paid())
    return None