from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import *
uri = "mongodb+srv://hazzy:hazzy1990@cluster0.s9aqskd.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
bd = connect(host=uri, ssl=True, db="hw8")
# Send a ping to confirm a successful connection
try:
    bd.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


