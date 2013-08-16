# Running App by
# Gowri Grewal
# Hackbright Final Project - August 2013
"""
model.py has the Class and model for this app
seed.py loads the seed data in the database
runcoach.db is the database, and there are 2 tables: Users and Assignments

OBJECTIVE:

Retrieve workout activities stored in a Garmin Forerunner 405cx GPS Watch.
Retrieve assigned workouts and training log from RunCoach and push the combined data to the web.

"""
from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

#this may be an opportunity to do screen scraping later...
@app.route("/")
def index():
    assignment_list = model.session.query(model.Assignment).order_by(model.Assignment.date).all()
    return render_template("index.html", assignments=assignment_list)

# Convert the assignment_list and running list into a dictionary:
# 	key is the date in MM-DD-YYYY format
# 	values are:
# 		assignment.type
# 		assignment.miles
# 		assignment.low_time.convert_time (hours minutes, seconds)
# 		assignment.high_time.convert_time (hours minutes, seconds)
# 		log.distance
# 		log.time.convert_time

# THEN, pull them out of the dictionary to display them












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

# # view a list of users
# @app.route("/users")
# def show_users():
#     user_list = model.session.query(model.User).all()
#     # ratings_list = model.session.query(model.Rating).all()
#     return render_template("users.html", users=user_list)

# # click on a user and view list of movies they've rated, as well as the ratings
# @app.route("/user_ratings")
# def show_user_ratings():
#     user_id = request.args.get("user_id")
#     ratings_list = model.session.query(model.Rating).filter_by(user_id=user_id).order_by(model.Rating.movie_id)
#     return render_template("user_ratings.html", user_id=user_id, ratings_list=ratings_list)

# # when logged in, be able to add or update a personal rating for a movie.
# @app.route("/change_rating")
# def change_rating():
#     rating_object=model.session.query(model.Rating).get(request.args.get("rating_id"))
#     movie=model.session.query(model.Movie).get(rating_object.movie_id)
#     user_rating=request.args.get("rating", False)
#     if user_rating:
#         rating_object.rating=user_rating
#         model.session.add(rating_object)
#         model.session.commit()
#     return render_template("change_rating.html",
#                             rating_id=rating_object.rating, 
#                             user_id=rating_object.user_id, 
#                             movie_id=rating_object.movie_id,
#                             movie=movie.name)

# @app.route("/add_rating")
# def add_rating():
#     user_id = request.args.get("user_id")
#     return render_template("add_rating.html", user_id=user_id)

# @app.route("/rating_added")
# def rating_added():
#     rating_id=request.args.get("rating_id")
#     rating=request.args.get("rating")
#     rating_object=model.session.query(model.Rating).get("rating_id")
#     movie=model.session.query(model.Movie).get(rating_object.movie_id)
#     return render_template("rating_added.html",
#                             rating_id=rating_id, 
#                             rating = rating,
#                             user_id=rating_object.user_id, 
#                             movie_id=rating_object.movie_id,
#                             movie=movie.name)
if __name__== "__main__":
    app.run(debug=True)
