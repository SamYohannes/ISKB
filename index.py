
# http://flask.pocoo.org/docs/1.0/

# pip is a Python package manager (like a vast plugin library)
# we use pip to install Flask, and the line below is how we bring in Flask (and
# a variety of other functions and helpers) into our app
from flask import Flask, url_for, render_template, jsonify, request
app = Flask(__name__)

# INDEX PAGE
# the '/' is removed by default by the browser, but it represents the root page
# (eg www.facebook.com/)
@app.route("/")
def index():
    # When we visit http://localhost:5000 or http://127.0.0.1:5000 (they're the
    # same thing) we fire this function which returns a string which is displayed
    # in the browser
    return render_template('./CarryOn.html')

app.static_folder = 'static'

@app.route("/AboutUs")
def Aboutus():

    return render_template('./AboutUs.html')

@app.route("/bruges")
def bruges():

    return render_template('./bruges.html')

@app.route("/Destinations")
def destinations():

    return render_template('./Destinations.html')

@app.route("/Findbuddy")
def findbuddy ():

    return render_template('./Findbuddy.html')

@app.route("/Germany")
def germany():

    return render_template('./Germany.html')

@app.route("/ireland")
def ireland():

    return render_template('./Ireland.html')

@app.route("/marseille")
def marseille():

    return render_template('./marseille.html')

@app.route("/paphos")
def paphos():

    return render_template('./paphos.html')

@app.route("/Porto")
def porto():

    return render_template('./Porto.html')

@app.route("/Rhonda")
def Rhonda():

    return render_template('./Rhonda.html')

@app.route("/Romania")
def romania():

    return render_template('./Romania.html')

@app.route("/Sweden")
def Sweden():

    return render_template('./Sweden.html')

@app.route("/Valletta")
def Valletta():

    return render_template('./Valletta.html')

@app.route("/Verona")
def Verona():

    return render_template('./Verona.html')


# POST EMAIL FORM ACTION
@app.route("/email", methods=['POST'])
def emailPost():
    send_simple_message(request.form['email'])
    return "Email was sent successfully"

# TEST ROUTES
# The below isn't necessary, it's just a way to test each route to make sure
# they do what you expect
with app.test_request_context():
    print(url_for('index'))

# What actually runs the app
app.run()
