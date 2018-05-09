import os
from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/CSI/WebSites/TestWebSite/sql/users.db'
db = SQLAlchemy(app)

class CreateTables(db.Model):

    def createData(self, db):
        __tablename__= 'new_users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100))
        password = db.Column(db.String(100))
        points = db.Column(db.Integer)

    def __init__(self, id, data):
        self.id = id
        self.username = data