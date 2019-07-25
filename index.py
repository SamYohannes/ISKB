

from flask import Flask, url_for, render_template, jsonify, request
app = Flask(__name__)


@app.route("/")
def index():

    return render_template('base.html')

app.static_folder = 'static'

@app.route("/CarryOn")
def CarryOn():

    return render_template('CarryOn.html')

@app.route("/AboutUs")
def Aboutus():

    return render_template('AboutUs.html')

@app.route("/bruges")
def bruges():

    return render_template('bruges.html')

@app.route("/Destinations")
def destinations():

    return render_template('Destinations.html')

@app.route("/Findbuddy")
def findbuddy ():

    return render_template('Findbuddy.html')

@app.route("/Germany")
def germany():

    return render_template('Germany.html')

@app.route("/Ireland")
def ireland():

    return render_template('Ireland.html')

@app.route("/marseille")
def marseille():

    return render_template('marseille.html')

@app.route("/paphos")
def paphos():

    return render_template('paphos.html')

@app.route("/Porto")
def porto():

    return render_template('Porto.html')

@app.route("/Rhonda")
def Rhonda():

    return render_template('Rhonda.html')

@app.route("/Romania")
def romania():

    return render_template('Romania.html')

@app.route("/Sweden")
def Sweden():

    return render_template('Sweden.html')

@app.route("/Valletta")
def Valletta():

    return render_template('Valletta.html')

@app.route("/verona")
def Verona():

    return render_template('Verona.html')

@app.route("/salzburg")
def salzburg():

    return render_template('salzburg.html')


@app.route("/email", methods=['POST'])
def emailPost():
    send_simple_message(request.form['email'])
    return "Email was sent successfully"




app.run()
