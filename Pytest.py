import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request
from WebCalendarAI import WebCalendarAI
from PageManager import PageManager
from Pages import Pages  
#from CreateTables import CreateTables
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/CSI/WebSites/TestWebSite/sql/users.db'
db = SQLAlchemy(app)

#Where to go.
@app.route('/')
#Method tied to app route.
def index():
    #names = db.excute("CREATE TABLE flight")
    #PageManage = PageManager()
    #page = Pages("main",'index.html')
    #PageManage.StoreHtml(page)
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    user = users(id=0, username=request.form['username'], password=request.form['password'], points=0)
    db.session.add(user)
    db.session.commit()
    return render_template('signup.html')
    
#route for the signup page.
@app.route('/signup')
def signup():
    #createTable()
    return render_template("signup.html")

@app.route('/days')
def days():
   return render_template("AvilableWeekDays.html")

@app.route('/createWorkOut')
def createDays():
    return render_template("squat.html")

@app.route('/calendar')
def calendar():
    months = createMonths()
    day = createDays()
    return render_template("calendar.html", days=day, month=months)
    
def createMonths():
    calendar = WebCalendarAI()
    txt = calendar.getCurrentMonths()
    return txt

def createDays():
    calendar = WebCalendarAI()
    days = calendar.getCurrentDays()
    return days

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    points = db.Column(db.Integer)

if __name__ == "__main__":
    app.run(debug=True)