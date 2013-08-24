Hackbright-Final-Project
========================

Repo for Gowri's Running App

OBJECTIVE:

Retrieve workout activities stored in a Garmin Forerunner 405cx GPS Watch.
Retrieve assigned workouts and training log from RunCoach and push the combined data to the web.
Generate data analysis to determine whether workout/training goals from RunCoach were met by runner.


UPDATE - 8/20/13 push:

Retrieve daily workout activities stored in a CSV file, downloaded from Garmin site

Retrieve daily assigned workouts from RunCoach in JSON format, via an http request to the Runcoach API

Display combined data on localhost

To run this program on your local machine:
    1. clone the directory
    2. run "python app.py"
    3. view app in localhost:5000

Code pushes beyond 8/20/13: Work in progress

FILES:
model.py - contains the database model and classes for the application

app.py - contains the web application and routes

seed.py - program used to seed the runcoach.db with data retrieved from Runcoach JSON object

seedGarmin.py - program used to seed the runcoach.db with data retrieved from Garmin CSV file

alembic/ - directory containing alembic configuration files to maintain revisions to the runcoach.db

TECHNOLOGIES USED:
Python
JavaScript
Sqlite3
Sqlalchemy
Flask
Jinja
