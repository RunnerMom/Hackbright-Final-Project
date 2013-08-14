GOWRI's WORKING NOTES:
=====================

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
- finished and ran seedGarmin.py - done for Time and Distance for ~9 days
- check db with python -i model.py -> using sqlalchemy commands
>>> log = session.query(Log).all()
>>> log[0].date
>>> session.query(Log).count()

5. Populate garmin table with 'real' data - done
============= 8.13.13 ========

6. Use alembic to track revisions of new class - done

7. Get something to display properly in html/flask on local machine
To-Do-Next:
- update model to:
	- convert dates to Datetime objects
	- Associate Log.date with Assigment.date as a foreign key.
	- Test calling Log.date.miles -> does date need to be primary key?
	- Sort the assignment-list and running-log
	- update model to save Hours, Seconds and Minutes separately for both Assignment and Log

- then, figure out how to get this to display properly
	- through app
	- or through flask/html








================next steps
*. More UI development
*. initial analysis of whether goal was met
*. Dynamic call to runcoach API




