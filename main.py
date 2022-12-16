#My Code
import db
import dbEdit as edit
#SQL-Alch

a=2

db.createDB()

edit.add_member('Cloud','tail','TC',11111,'Camp')

print(f'{edit.findID(a).fname}{edit.findID(a).lname}')