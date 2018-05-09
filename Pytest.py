import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request, redirect, jsonify
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

@app.route('/days', methods=['GET','POST'])
def days():
    if request.method == 'POST':
        #days = request.form['days']
        #text = str(days[2])
        return render_template("avdays.html") 
        #return jsonify({days: text})
        #for day in days:
         #   print(name)
    else:
        return render_template("signup.html")       

    #days = request.form['days']
    #return jsonify({'days': days})

@app.route('/add', methods=['POST'])
def add():
    user = users(username=request.form['username'], password=request.form['password'], points=0)
    db.session.add(user)
    db.session.commit()
    return render_template("continue.html")

#route for the signup page.
@app.route('/signup')
def signup():
    #createTable()
    return render_template("signup.html")

@app.route('/goDays', methods=['POST'])
def goDays():
    if request.method == 'POST':
        days = request.form['days']
        text = str(days[2])
        return jsonify({days: text})


@app.route('/createWorkOut')
def createDays():
    return render_template("squat.html")

@app.route('/calendar')
def calendar():
    months = createMonths()
    day = createDays()
    return render_template("calendar.html", days=day, month=months)

@app.route('/squat')
def squat():
    return render_template('squat.html')

@app.route('/bench')
def bench():
    return render_template('bench.html')
    
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