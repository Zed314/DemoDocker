from flask import Flask,redirect,url_for
from pymongo import MongoClient, InsertOne
app = Flask(__name__)

client = MongoClient('mongodb://sampledb:27017/')
sampleDB = client["sample"]
names = sampleDB["names"]

@app.route('/')
def listName():
    messageToSendBack =""
    for name in names.find({}) :
	    messageToSendBack += (name["name"]+",")
    return messageToSendBack

@app.route('/add/<string:nameToAdd>')
def addName(nameToAdd):

    
    names.bulk_write([InsertOne({ "name": nameToAdd} )])
    return redirect(url_for('listName'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    