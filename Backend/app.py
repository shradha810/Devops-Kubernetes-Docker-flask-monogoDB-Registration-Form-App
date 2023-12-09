from flask import Flask, request
import pymongo
import os

Mongo = os.environ.get('MONGO')
client = pymongo.MongoClient(Mongo)
### cluster:ShradhaLearn database:test collection:flask-signup ###
db = client.test
collection = db['flask-signup']

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json) 
    collection.insert_one(form_data)
    return 'Data Added to mongoDB'

@app.route('/data')
def data():
    content = list(collection.find())
    for elm in content:
        del(elm['_id'])
    return {
        'Content': content
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8500,debug=True)
