from flask import Flask
import pymongo
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
client=pymongo.MongoClient('localhost',27017)
db=client[ 'bedman']



from app import routes
from hospital import routes
from hospital import models

