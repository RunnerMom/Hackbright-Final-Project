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
    logs = relationship("Log", backref="assignment", uselist=True)
    date= Column(Date, nullable = False)   # calendar date
    workout_type = Column(String(64), nullable = True)
    miles = Column(Float)
    low_time = Column(Integer)
    high_time = Column(Integer)

    def convert_seconds(self, time_in_seconds):
        hours = floor(time_in_seconds/3600) #int
        minutes = floor((time_in_seconds/60)-hours*60)  #int
        seconds = time_in_seconds - 3600*hours - 60*minutes #int
        text = "%d:%02d" % (hours, minutes) #string
        return {"hours": hours, 
                "minutes": minutes,
                "seconds": seconds,
                "text": text}
    def logs_distance(self):   #sum the total distance in assignment.logs
        return reduce(lambda a,i: sum(a, (float(i.distance))), self.logs) 

    def logs_time(self):      #sum the total distance in assignment.logs
        return reduce(lambda a,: 
            a+float(i.convert_timestring()["totalseconds"]), 
            self.logs)

        #   log[i].time is a timestring
        #   dict = convert_timestring(list[i].time) is a dictionary
        #   dict["totalseconds"] = integer of seconds

class Log(Base):        #this is the data from Garmin
    import datetime
    __tablename__= "logs"     
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    date= Column(Date)   # calendar date
    distance = Column(String)
    time = Column(String)
    def convert_timestring(self):   #takes in a log object
        timelist=self.time.split(":")
        if len(timelist)==3:
            hours = int(timelist[0])
            minutes = int(timelist[1])
            seconds = float(timelist[2])
        elif len(timelist)==2:
            minutes = int(timelist[0])
            seconds = float(timelist[1])
        text = "%d:%02d:%02d" % (hours, minutes, seconds)
        totalseconds = hours*3600+minutes*60+seconds
        return {"hours": hours, 
                "minutes": minutes,
                "seconds": seconds,
                "text": text,
                "totalseconds": totalseconds}

    def convert_distance(self, string):
        miles = float(string)
        meters = miles*1609.344

### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
