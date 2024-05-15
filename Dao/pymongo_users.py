from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rlatjdtn1014:<pw>@cluster0.q7dnljt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.user


def connectTest():    
    # Create a new client and connect to the server
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def getUsers():
    col = db.info
    data = col.find()
    return data

def setUsers(name, age):
    col = db.info
    col.insert_one({"name":name,"age":age})
    


# bdmzs2xozrgoTxv6