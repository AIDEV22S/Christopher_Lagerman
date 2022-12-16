#My Code
import db
import dbEdit as edit
import gui
#SGUI
import PySimpleGUI as sg

window = gui.getWindow()
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED or 'Exit'):
        break

    if event == 'Add Member':
        winTwo = gui.get_add_window()
        while True:
            eventwo, valuesTwo = winTwo.read()

            if event in(sg.WINDOW_CLOSED or 'Exit'):
                break





window.close

exit()