#My Code
import db
import dbEdit as edit
#SQL-Alch

a=2

db.createDB()

edit.add_member('John','Smith','Streetname 1',11111,'Stockholm')

print(f'{edit.findID(a).fname}{edit.findID(a).lname}')