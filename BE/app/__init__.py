from flask import Flask
import pymongo

app = Flask(__name__)

client=pymongo.MongoClient('localhost',27017)
db=client[ 'bedman']



from app import routes
from hospital import routes
from hospital import models

