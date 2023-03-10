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
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
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
            if eventwo == 'Clear':
                gui.clear_add(winTwo)

            if eventwo == 'Cancel':
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
                    mID = valuesTwo['fID']
                    found = edit.findID(valuesTwo['fID'])
                    winTwo.close()


# Update Member
                    winTwo = sg.Window('Manage member.',gui.get_updateLayout(found))

                    while True:
                        eventwo, valuesTwo = winTwo.read()


                        if eventwo == sg.WINDOW_CLOSED:
                            break

                        if eventwo == 'Exit':
                            winTwo.close()
                            break


                        if eventwo == 'Toggle Paid Membership':
                            found.update_paid()
                            gui.updateInfo(winTwo, found)

                        if eventwo == 'Delete Member':
                            winTwo.close()
                            gui.update_msg('Member deleted')
                            edit.delete_member(mID)
                except:
                    gui.update_msg('Failed to find Member.')
                break
            if eventwo == 'Cancel':
                winTwo.close()
                break


window.close

exit()