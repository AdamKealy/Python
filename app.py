from flask import Flask, request

import datetime

app = Flask(__name__)


@app.get("/")       #HTTP request:  GET /
def index():
    ##return datetime.datetime.now().ctime()
    with open("index.html") as f:
        html = f.read()
    return html

@app.get("/hello")  #HTTP request:  GET /hello
def hello():
    return "Hello from my first flask webapp. it's your fault."


@app.get("/showform")
def display_form():
    """
        Retrieve the form.html file from the hard disk, and send it to the
        browser.
    """
    with open("form.html") as f:
        html = f.read()
    return html

@app.post("/processform")
def save_data():
    """
        Recieve the data from the HTML form, then save it to a disk file, then respond
        with a nice friendly message to the awaiting browser.

        The following inputs are expected: first, last and dob.
    """
    # python-name = html-name:
    the_first = request.form["first"]
    the_last = request.form["last"]
    the_dob = request.form["dob"]
    # So...... now use the python -names in your code
    with open("suckers.txt", "a") as sf:
        print(f"{the_first}, {the_last}, {the_dob}", file=sf)
    return f"Thanks, {the_first}, we promise not to sell your data to the bad guys."




if __name__== "__main__":
    app.run(debug=True)
