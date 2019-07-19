from flask import Flask, request
from flask_restful import Resource, Api
from parse import parse
from molarmass import molarMass
from combustion import combust
import json

app = Flask(__name__)
api = Api(app)

elements = {}

class MolarMass(Resource):
    def get(self, element_id):
        return {element_id: elements[element_id]}
    def put(self, element_id):
        elements[element_id] = molarMass(request.form['data'])
        return {element_id: elements[element_id]}
    
class Combust(Resource):
    def get(self, element_id):
        return {element_id: elements[element_id]}
    def put(self, element_id):
        elements[element_id] = combust(request.form['data'])
        return {element_id: elements[element_id]}

api.add_resource(MolarMass, '/molarmass/<string:element_id>')
api.add_resource(Combust, '/combust/<string:element_id>')

if __name__ == '__main__':
    app.run(debug=True)
