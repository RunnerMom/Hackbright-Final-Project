import model
model.Base.metadata.create_all(model.engine)        #code review with db instructor 

import csv
# import time
from datetime import datetime
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
This program is built to load garmin data into a runcoach.db sqlite3 database:
load_activity -> loads the user's daily activies into Log table
"""
def convert_date_string(date_string):
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return dt.date()

def load_activity():
    with open('seed_data/Garmin/ActivityData.csv') as csvfile:
        run_data = csv.reader(csvfile, delimiter=',')

     #   print "length of list:", len(list(running_data)) 
        for row in run_data:
            date = row[0] #string
            converted_date = convert_date_string(date)  #convert to date object
            assignment = model.session.query(model.Assignment).filter_by(date=converted_date).first()
            time = row[2]
            distance = row[4]
            running_log = model.Log(date = converted_date, time = time, distance = distance, assignment_id=assignment.id)
            session.add(running_log)
        session.commit()
       #     print date + " : " + time + " minutes, " + distance + " miles"

         
def main():
    # You'll call each of the load_* functions with the session as an argument
    load_activity()

if __name__ == "__main__":
#     s=model.connect()
    main()
