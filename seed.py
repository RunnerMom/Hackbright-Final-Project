import model
model.Base.metadata.create_all(model.engine)        #code review with db instructor 
import json
import time
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import ForeignKey
from urllib2 import urlopen

engine = create_engine("sqlite:///runcoach.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()
"""
This program is built to load runcoach data into a runcoach.db sqlite3 database:
load_users - > user data
load_types -> workout types
load_assignment -> user's daily workout assignment
"""
def convert_date_string(date_string):
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return dt.date()

def load_assignment():
    assignment = urlopen("http://runcoach.com/get_schedule_json.php?p_fnf_token=26444eb8030137c06ddd67e10caef3f3546f6bdc&p_request_id=32148&p_ath_id=474&p_from_date=2014-01-01&p_to_date=2014-01-30")
    assignment_data = json.load(assignment)
    for key, value in assignment_data.items():
        converted_date = convert_date_string(key)
        workout_type = value['WoTypeName']
        miles = value['miles']
        low_time_in_seconds = value['lotime']
        high_time_in_seconds = value['hitime']
        assignment_record = model.Assignment(date=converted_date, workout_type=workout_type, miles=miles, low_time=low_time_in_seconds, high_time=high_time_in_seconds)
        session.add(assignment_record)
    session.commit()


# def load_movies(session):
#     with open('seed_data/u.item') as csvfile:
#         movie_data = csv.reader(csvfile, delimiter='|')
#         print ("Loading movie db. This could take several minutes")
#         for row in movie_data:

#             row_time = row[2]   #this is the non-formatted datetime
#             row_name = row[1]   #this is the movie title
#             row_name = row_name.decode("latin-1")   #this gets rid of accents
#             row_name_list = row_name.split(' ')     #creates a list
            
#             if len(row_name_list) > 1:      # if title + year, then pop off the year and save the title only
#                 row_name_list.pop()
#                 movie_title = " ".join(row_name_list)
#             else:
#                 movie_title = " ".join(row_name_list)  #if title only, convert back to string

#             # try to make an error handler to skip data that does not have proper date formatting

#             if row_time:
#                 last_date = convert_date_string(row_time) #creates a Python datetime object
#                # print last_date 
#                 movie_record = model.Movie(id = row[0], name=movie_title, released_at=last_date, imdb_url=row[4]) #populates movie record
#                 session.add(movie_record)
#         session.commit()

# def load_ratings(session):
#     with open('seed_data/u.data') as csvfile:
#         ratings_data = csv.reader(csvfile, delimiter='\t')
#         for row in ratings_data:

#             row_timestamp=row[3]
#             new_timestamp = convert_epoch_time(row_timestamp)

#             ratings_record = model.Rating(user_id=row[0], movie_id=row[1], rating=row[2], timestamp=new_timestamp)
#             session.add(ratings_record)
#         session.commit()
         
def main():
    # You'll call each of the load_* functions with the session as an argument
    load_assignment()

if __name__ == "__main__":
#     s=model.connect()
    main()
