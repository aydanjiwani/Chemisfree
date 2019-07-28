from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from parse import parse
from molarmass import molarMass
from combustion import combust
import json

app = Flask(__name__)
api = Api(app)
CORS(api)


class MolarMass(Resource):
    def get(self, element_id):
        return {element_id: molarMass(element_id)}

class Combust(Resource):
    def get(self, element_id):
        return {element_id: combust(element_id)}
    

api.add_resource(MolarMass, '/molarmass/<string:element_id>')
api.add_resource(Combust, '/combust/<string:element_id>')

if __name__ == '__main__':
    app.run(debug=True)
