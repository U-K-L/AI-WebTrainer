import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')



engine = create_engine("postgres://kwyoldtqbouptt:f7127c443551c5b8d363c91d3fd54dd7c9967d64db7e40d82b9d6ea371366b23@ec2-174-129-28-38.compute-1.amazonaws.com:5432/d6g2qqn2orkcf2")
db = scoped_session(sessionmaker(bind = engine))

#Where to go.
@app.route('/')
#Method tied to app route.

def index():
    #names = db.excute("CREATE TABLE flight")
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)