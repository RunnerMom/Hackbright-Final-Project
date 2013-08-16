from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import ForeignKey
from math import floor

engine = create_engine("sqlite:///runcoach.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

""" 
The classes below are tables in our runcoach.db
"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    token = Column(String(64), nullable=True)
    request_id = Column(String(64), nullable=True)
    ath_profile_id = Column(Integer, nullable=True)

class Assignment(Base):
    import datetime
    __tablename__= "assignments"     
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    logs = relationship("Log", backref="assignment")
    date= Column(Date, nullable = False)   # calendar date
    workout_type = Column(String(64), nullable = True)
    miles = Column(Float)
    low_time = Column(Integer)
    high_time = Column(Integer)

    def convert_seconds(self, seconds):
        hours = floor(seconds/3600)
        minutes = (seconds/60)-hours*60
        return "%d:%02d" % (hours, minutes)
    
"""
class Workout(Base):             
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    workout_type = Column(Integer, nullable=True)
    pace = Column(String(16), nullable=True)
    workout_time = Column(Time, nullable=True)
"""

class Log(Base):
    import datetime
    __tablename__= "logs"     
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    date= Column(Date)   # calendar date
    distance = Column(String)
    time = Column(String)
    # def convert_time(self, string):
        # hours = 
        # minutes = 
        # return "%d:%02d" % (hours, minutes)
    # def convert_distance(self, string):
        # miles = 
        # meters = 

### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
