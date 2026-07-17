from pymongo import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://aboral:Anitra06@cluster0.m1579e6.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
