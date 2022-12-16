from sqlalchemy import create_engine,update,delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

import db


'''New members will be set to "paid" by default. I'm assuming they are added after
the initial payment is aproved.'''

def add_member(fname, lname,address,postnr,postaddr):
    member = db.Member(fname,lname,address,postnr,postaddr)
    db.session.add(member)
    db.session.commit()


def update_paid(mID,pStat):
    x = db.session.get(db.Member,mID)
    x.update_paid(pStat)
    db.session.commit

def findID(mID):
    return db.session.get(db.Member,mID)


