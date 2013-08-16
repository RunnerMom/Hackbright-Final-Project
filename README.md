Hackbright-Final-Project
========================

Repo for my Garmin-Runcoach project

OBJECTIVE:

Retrieve workout activities stored in a Garmin Forerunner 405cx GPS Watch.
Retrieve assigned workouts and training log from RunCoach and push the combined data to the web.


UPDATE - current status:

Retrieve daily workout activities stored in a CSV file, downloaded from Garmin site

Retrieve daily assigned workouts in JSON format, via an http request to the Runcoach API

Display combined data on localhost

To run this program on your local machine:
    1. clone the directory
    2. run "python app.py"
    3. view app in localhost:5000

FILES:
model.py - contains the database model and classes for the application

app.py - contains the web application and routes

seed.py - program used to seed the runcoach.db with data retrieved from Runcoach JSON object

seedGarmin.py - program used to seed the runcoach.db with data retrieved from Garmin CSV file

alembic/ - directory containing alembic configuration files to maintain revisions to the runcoach.db