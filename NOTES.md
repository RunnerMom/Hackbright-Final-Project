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

WEB SCRAPING: http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/

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
========== 8.2.13 field trip =========
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
DOne:
- update model to:
	- convert dates to Datetime objects
	- Associate Log.date with Assigment.date as a foreign key.
	- Test calling Log.date.miles -> does date need to be primary key?
	- instead of pulling from the db and saving to a list, save to a dictionary with the date as the key.
- NEXT: When working with the display today, I realized that my schema had not been designed well. Played with alembic for a minute, then was advised to delete my db and re-create with new schema

=========== 8.14.13 ==========
Done:
- Re-created db:
	- saved old db to old_.db
	- re-did schema in model.py
	- re-did seed.py to take in a URL from runcoach
	- from python -i model.py:
		- ** need to Base.metadata.drop_all(bind=engine)
		- ** need to Base.metadata.create_all(bind=engine)
		- This drops the schema and re-creates. Maybe this is a step that gets saved by alembic?????
	- checked that db re-populated (runcoach)correctly
========8.15.13 =========
Done:
- re-populate Garmin data with month of July
- checked that Garmin populated correctly
=======8.16.13 ===========
- sorted the dictionary in date order
- Associated the Log class with the Assignment class:
	- added assignment_id to Log class as foreignkey. Added logs as backref to Assignment class.
	- removed foreignkey based on date.
	- when seeding the garmin data, for each log:
	   - converted date_string to date object
	   - queried assignment table for that date
	   - added the assignment_id for the corresponding assignment as an attribute of that log
- because of this association, flask now only needs to query the assignment object and can get all the info from the log(s) for that assignment. So, updated index page to reflect this.
- now displays logs for each assignment on same row!

To Do:
- create a git branch: 
git branch <name>
git checkout <name>
	- write some code to compare the mileage run vs assignment
			- update model to save Hours, Seconds and Minutes separately for both Assignment and Log
	- add a Twitter Bootstrap template
	- change index page to:
		- select user
		- select dates to download from Rcoach -> download button
		- select dates to download from Garmin -> download button
		- create a "clear database" option for the demo
	- figure out how to 
- add a couple users (?)

================next steps ===========
*. More UI development
*. initial analysis of whether goal was met
*. Dynamic call to runcoach API




