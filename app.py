from flask import Flask, render_template, request, session
from flask_session import Session 
import datetime

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# @app.route("/")
# def index():
#     return "hello, world!!!e!!"


@app.route("/leo")
def leo():
    return "hello leo"

# @app.route("/<string:name>")
# def hello(name):
#     name = name.capitalize()
#     return f"<h1>hello {name}</h1>"

#-------------

# @app.route("/")
# def index():
#     return render_template("index.html")

#-------------

# @app.route("/")
# def index():
#     headline = "Hello worlddd"
#     return render_template("index.html", headline=headline)

#------

# @app.route("/")
# def index():
#     now = datetime.datetime.now()
#     new_year = now.month == 1 and now.day == 1
#     headline = "Hello worlddd"
#     names =["Alice", "Bob","Charlie"]
#     return render_template("index.html", headline=headline, new_year= new_year,names=names)


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html",name = name)


#---------------------


@app.route("/", methods = ["GET","POST"])
def index():
    if session.get("notes") is None:
        session["notes"] =[]
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html",notes = session["notes"])




