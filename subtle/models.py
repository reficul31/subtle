from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))
db = SqliteExtDatabase(os.path.join(basedir, 'subtle.db'))

class BaseModel(Model):
    class Meta:
        database = db

class Point(BaseModel):
    title = CharField(unique=True)
    dir = CharField(unique=True)

def initdb():
	print("Making the Database tables")
	db.connect()
	db.create_tables([Point,])