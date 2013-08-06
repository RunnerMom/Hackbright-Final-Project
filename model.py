from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///runcoach.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

""" 
The 3 classes below are tables in our runcoach.db
"""
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    token = Column(String(64), nullable=True)
    request_id = Column(String(64), nullable=True)
    ath_profile_id = Column(Integer, nullable=True)

class Assignment(Base):
    import datetime
    __tablename__= "assignments"     #when do we use u.item instead of "movie?"

    id = Column(Integer, primary_key = True)
    date= Column(String(64), nullable = True)   # calendar date
#    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=True)
    workout_type = Column(String(64), nullable = True)
    miles = Column(Float)
    low_time = Column(Integer)
    high_time = Column(Integer)
    def seconds_to_minutes(self, seconds):
        hours = seconds/3600
        minutes = seconds/60
        timestring = "%h : %m" % hours, minutes
        return timestring
    
"""
class Workout(Base):             #u.data = "rating" ??
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    workout_type = Column(Integer, nullable=True)
    pace = Column(String(16), nullable=True)
    workout_time = Column(Time, nullable=True)


class Log(Base):
    assigment_ID
    MILES_COMPLETED
    pace
    workout_time
### End class declarations

"""
def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
