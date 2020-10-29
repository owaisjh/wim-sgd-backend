from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import LandmarkAdd




import json


from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'safety'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=99999999999)

jwt = JWT(app, authenticate, identity)  # authentication





api.add_resource(LandmarkAdd, '/landmark_add')








if __name__ == "__main__":
    app.run(port=5000, debug=True)
