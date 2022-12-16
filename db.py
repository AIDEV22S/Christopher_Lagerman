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
    address = Column(String)
    postnr = Column(Integer)
    postaddr = Column(String)
    paid = Column(Boolean)

    def __init__(self, fname, lname,address,postnr,postaddr,paid=True):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.postnr = postnr
        self.postaddr = postaddr
        self.paid = paid
    def update_paid(self,pStat):
        self.paid = pStat


def createDB():
    Base.metadata.create_all(engine)