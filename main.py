#My Code
import db
import dbEdit as edit
import gui
#SGUI
import PySimpleGUI as sg

window = gui.getWindow()
while True:
    event, values = gui.winRead()
    if event in (sg.WINDOW_CLOSED or 'Exit'):
        break

    if event == 'Clear':
        gui.clear_UI()

    if event == 'Ok':
        gui.ok_pressed(values['nameInpput'])

window.close

exit()