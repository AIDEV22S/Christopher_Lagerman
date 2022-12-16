#My Code
import db
import dbEdit as edit
import gui
#SGUI
import PySimpleGUI as sg

db.createDB()

window = gui.getWindow()

input_msg = ''
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED or 'Exit'):
        break

#add member
    if event == 'Add Member':
        winTwo = sg.Window('Add Member.',gui.get_addLayout())

        while True:
            eventwo, valuesTwo = winTwo.read()

            if eventwo == sg.WINDOW_CLOSED:
                break

            if eventwo == 'OK':
                try:
                    edit.add_member(
                    valuesTwo['fnameInput'],
                    valuesTwo['lnameInput'],
                    valuesTwo['adressInput'],
                    valuesTwo['pnrInput'],
                    valuesTwo['padrInput'])


                    gui.update_msg(f'Success, added new member: '
                    f'{valuesTwo["fnameInput"].capitalize()} {valuesTwo["lnameInput"].capitalize()}')
                except:
                    gui.update_msg('Invalid input.')
            winTwo.close()

#Find Member
    if event == 'Find Member':
        winTwo = sg.Window('Find Member.',gui.get_findLayout())

        while True:
            eventwo, valuesTwo = winTwo.read()

            if eventwo == sg.WINDOW_CLOSED:
                break

            if eventwo == 'Search':
                try:

                except:
                    print('invalid ID')


#Update Member
    if event == 'Update Member':
        print('Not yet done.')





window.close
exit()