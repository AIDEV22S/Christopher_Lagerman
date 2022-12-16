from sqlalchemy import create_engine,update,delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean


engine = create_engine('sqlite:///C:\\dbfiles\\mydb.db')
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    adress = Column(String)
    postnr = Column(Integer)
    postadr = Column(String)
    paid = Column(Boolean)

    def __init__(self, fname, lname,adress,postnr,postadr,paid=True):
        self.fname = fname
        self.lname = lname
        self.adress = adress
        self.postnr = postnr
        self.postadr = postadr
        self.paid = paid
    def update_paid(self):
        if self.paid:
            self.paid = False
        else:
            self.paid = True

    #get data
    def get_name(self):
        return f'{self.fname} {self.lname}'
    def get_adr(self):
        return self.adress
    def get_post(self):
        return f'{self.postadr}, {self.postnr}'
    def get_paid(self):
        return self.paid



def createDB():
    Base.metadata.create_all(engine)

def getSession():
    return session