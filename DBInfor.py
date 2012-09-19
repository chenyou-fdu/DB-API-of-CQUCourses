# –*- encoding:utf8 –*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql://root:1@localhost/c_test?charset=utf8')
Base = declarative_base()
class CQUCourses(Base):
    __tablename__ = 'cqucourses'
    ID = Column(Integer, primary_key=True)
    C_ID = Column(String)
    C_NAME = Column(String)
    I_ID = Column(String)
    C_INSTRUCTOR = Column(String)
    C_WEEK = Column(Integer)
    C_DAY = Column(Integer)
    C_SECTION = Column(String)
    C_LOCATION = Column(String)
    C_HOURS_IN_CLASS = Column(String)
    C_HOURS_IN_LAB = Column(String)
    C_CREDIT = Column(Float)
    C_SCHOOL = Column(String)

    def __init__(self, ID, C_ID, C_NAME, I_ID, C_INSTRUCTOR,\
                 C_WEEK, C_DAY, C_SECTION, C_LOCATION, C_HOURS_IN_CLASS, \
                 C_HOURS_IN_LAB, C_CREDIT, C_SCHOOL):
        self.ID = ID
        self.C_ID = C_ID
        self.C_NAME = C_NAME
        self.I_ID = I_ID
        self.C_INSTRUCTOR  = C_INSTRUCTOR
        self.C_WEEK = C_WEEK
        self.C_DAY = C_DAY
        self.C_SECTION = C_SECTION
        self.C_LOCATION = C_LOCATION
        self.C_HOURS_IN_CLASS = C_HOURS_IN_CLASS
        self.C_HOURS_IN_LAB = C_HOURS_IN_LAB
        self.C_CREDIT = C_CREDIT
        self.C_SCHOOL = C_SCHOOL

    def getAll(self):
        return [self.ID, self.C_ID, self.C_NAME, self.I_ID, self.C_INSTRUCTOR, \
                self.C_WEEK, self.C_DAY, self.C_SECTION, self.C_LOCATION, self.C_HOURS_IN_CLASS, \
                self.C_HOURS_IN_LAB, self.C_CREDIT, self.C_SCHOOL]


class InfoGet:
    def __init__(self,user,password,databases):
        #self.engine = create_engine('mysql://root:1@localhost/c_test?charset=utf8')
        url = 'mysql://'+user+':'+password+'@localhost/'+databases+'?charset=utf8'
        self.engine = create_engine(url)
        Session = sessionmaker(bind = self.engine)
        self.session = Session()

    def returnSession(self):
        return self.session













