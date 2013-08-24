# Running App by
# Gowri Grewal
# Hackbright Final Project - August 2013
"""
model.py has the Class and model for this app
seed.py loads the seed data in the database
runcoach.db is the database, and there are 2 tables: Logs and Assignments

OBJECTIVE:

Retrieve workout activities stored in a Garmin Forerunner 405cx GPS Watch.
Retrieve assigned workouts and training log from RunCoach and push the combined data to the web.

"""
from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    # queries Assignment table in runcoach.db, retrieves all assignment, in order by date
    assignment_list = model.session.query(model.Assignment).order_by(model.Assignment.date).all()
    return render_template("index.html", assignments=assignment_list)

@app.route("/device")
def device():
    return render_template("garmin_find_devices.html")

@app.route("/device_data", methods = ['POST'])
def device_data():
    # save the device data in the database
    # return 200
    return "Device data post received"

@app.route("/smoketest")
def smoketest():
    return "App appears to be OK, and test fixture is working."

# @app.route("/login")
# def login():
#     user_id = request.args.get("user_id")
#     password = request.args.get("password")
#     ratings_list = model.session.query(model.Rating).filter_by(user_id=user_id).order_by(model.Rating.movie_id)
#     return render_template("loggedin.html", user_id=user_id, ratings_list=ratings_list)

# @app.route("/add_user")
# def add_user():
#     age = request.args.get("age")
#     gender = request.args.get("gender")
#     occupation = request.args.get("occupation")
#     zipcode = request.args.get("zipcode")
#     user = model.User(age=age, gender=gender, occupation=occupation, zipcode=zipcode)
#     model.session.add(user)
#     model.session.commit()
#     return render_template("user_added.html", user_id=user.user_id)


if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')
