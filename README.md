Hackbright-Final-Project
========================

Repo for my Garmin-Runcoach Final project

OBJECTIVE:

Retrieve workout activities stored in a Garmin Forerunner 405cx GPS Watch.
Retrieve assigned workouts and training log from RunCoach and push the combined data to the web.


REFERENCES:

JSON overview http://www.json.org/
JSON tutorial http://www.w3schools.com/json/default.asp
JSON viewer http://jsonviewer.stack.hu/
JSON validator http://jsonlint.com/
GARMIN API http://developer.garmin.com/web-device/garmin-communicator-plugin/
Flask tutorial http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


Python/JSON: http://docs.python.org/2/library/json.html
http://effbot.org/zone/python-with-statement.htm

========== 8.1.13
1. Data Model for Runcoach
 - finish seed.py - done for Long Runs and Maintenance
 - check db with model -i mode sqlalchemy - done

>>> assignment = session.query(Assignment).filter_by(workout_type="Long Run")
>>> assignment[0].date
>>> session.query(Assignment).count()

2. Populate assignment table with 'real' data - done. ~9 assignments 
>>> done

3. Get something to display properly in html/flask on local machine
>>> done
========== 8.6.13
============= 8.8.13 ======= half day
============= 8.9.13 ======= conference day

4. Data Model for Garmin API

5. Populate garmin table with 'real' data
6. Get something to display properly in html/flask on local machine

============= 8.13.13 ========
7. More UI development
8. initial analysis of whether goal was met
9. More advanced assignment types




