# Laptop Service

from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient
import os

# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

class All(Resource):
    def get(self, top=0):  # defaulting to 0 because if someone wants the first 0 entries, they just won't go to the page
        if top:
            data = []
            for i in range(top):
                data.append(db.tododb.find_one())
        else:
            data = db.tododb.find()
        open_close = {}
        for pair in data:
            name = pair['name']
            desc = pair['description']
            open_close[name] = desc
            
        return open_close

class Open(Resource):
    def get(self, top=0):  #TODO add arg n
        data = db.tododb.find()  #TODO only find first n
        opens = {}
        for pair in data:
            name = pair['name']
            desc = pair['description']
            open_time = desc[0]
            opens[name] = open_time
        return opens

class Close(Resource):
    def get(self, top=0):
        data = db.tododb.find()
        closures = {}
        for pair in data:
            name = pair['name']
            desc = pair['description']
            close_time = desc[1]
            closures[name] = close_time
        return closures

class AllCSV(Resource):
    def get(self, top=0):
        data = db.tododb.find()
        csv = "km, open, close\n"  # column header
        for pair in data:
            name = pair['name']
            desc = pair['description']
            open_time = desc[0]
            close_time = desc[1]
            csv += name + ', ' + open_time + ',' + close_time + '\n'
        return csv

class OpenCSV(Resource):
    def get(self, top=0):
        data = db.tododb.find()
        opens = "km, open\n"  # column header
        for pair in data:
            name = pair['name']
            desc = pair['description']
            open_time = desc[0]
            opens += name + ', ' + open_time + '\n'
        return opens

class CloseCSV(Resource):
    def get(self, top=0):
        data = db.tododb.find()
        closures = "km, close\n"  # column header
        for pair in data:
            name = pair['name']
            desc = pair['description']
            close_time = desc[1]
            closures += name + ', ' + close_time + '\n'

# Create routes
# Another way, without decorators
api.add_resource(All, '/', '/listAll', '/listAll/json', '/?top=<int:top>', '/listAll?top=<int:top>', '/listAll/json?top=<int:top>', '/listAll/', '/listAll/json/')  # Adding option for '/' at the end in case the browser automatically adds it

api.add_resource(Open, '/listOpenOnly', '/listOpenOnly/json', '/listOpenOnly?<int:top>', '/listOpenOnly/json?<int:top>', '/listOpenOnly/', '/listOpenOnly/json/')

api.add_resource(Close, '/listCloseOnly', '/listCloseOnly/json', '/listCloseOnly/', '/listCloseOnly/json/')

api.add_resource(AllCSV, '/listAll/csv', '/listAll/csv/')
api.add_resource(OpenCSV, '/listOpenOnly/csv', '/listOpenOnly/csv/')
api.add_resource(CloseCSV, '/listCloseOnly/csv', '/listCloseOnly/csv/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
