from flask import Flask

import datetime

app = Flask(__name__)


@app.get("/")       #HTTP request:  GET /
def index():
    return datetime.datetime.now().ctime()

@app.get("/hello")  #HTTP request:  GET /hello
def hello():
    return "Hello from my first flask webapp. it's your fault"


if __name__== "__main__":
    app.run(debug=True)
