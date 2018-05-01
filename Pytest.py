import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')



engine = create_engine("postgres://kwyoldtqbouptt:f7127c443551c5b8d363c91d3fd54dd7c9967d64db7e40d82b9d6ea371366b23@ec2-174-129-28-38.compute-1.amazonaws.com:5432/d6g2qqn2orkcf2")
db = scoped_session(sessionmaker(bind = engine))

#Where to go.
@app.route('/')
#Method tied to app route.
def index():
    #names = db.excute("CREATE TABLE flight")
    if request.method == "POST":
        return "Hello World"
    else:
        return render_template('index.html')

#route for the signup page.
@app.route('/signup')
def signup():
   return render_template("signup.html")

@app.route('/nutrition')
#Method for nutrition route.
def nutrition():
    return "hello world"

    
if __name__ == "__main__":
    app.run(debug=True)