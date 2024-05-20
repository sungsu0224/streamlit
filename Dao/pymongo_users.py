import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["mongodb_uri"]

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
    data = list(col.find())
    return data

def setUsers(academy,classes,name, phone,age,parentPhone,link):
    col = db.info
    col.insert_one({"academy":academy,"classes":classes,"name":name,"phone": phone,"age":age,"parentPhone":parentPhone,"link":link})

def updateUsers(id,classes, name,phone,age,parentPhone):
    col = db.info
    col.update_one({"_id": id},{"$set":{"classes" : classes,"name": name,"phone" : phone , "age" : age, "parentPhone": parentPhone}})
