from sqlalchemy import create_engine,update,delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

import db

session = db.getSession()


'''New members will be set to "paid" by default. I'm assuming they are added after
the initial payment is aproved.'''

def add_member(fname, lname,adress,postnr,postadr):
    member = db.Member(fname.capitalize(),lname.capitalize(),adress.capitalize(),int(postnr),postadr.capitalize())
    session.add(member)
    session.commit()


def update_paid(mID):
    x = session.get(db.Member,mID)
    x.update_paid()
    session.commit

def findID(mID):
    return session.get(db.Member,int(mID))


