import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
#import base64
import datetime
import psycopg2




class User:
    def __init__(self, _id, username, password,  user_name, address, contact):
        self.id = _id
        self.username = username
        self.password = password
        self.user_name = user_name
        self.address = address
        self.contact = contact



    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not None:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
            connection = sqlite3.connect('user.db')
            cursor = connection.cursor()

            query = "SELECT * FROM users WHERE id=?"
            result = cursor.execute(query, (_id,))
            row = result.fetchone()
            if row is not None:
                user = cls(*row)
            else:
                user = None

            connection.close()
            return user



class PresOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    parser.add_argument('pres',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")
    #@jwt_required()
    def post(self):
        data = PresOrder.parser.parse_args()
        '''
        imgdata = base64.b64decode(data['pres'])
        filename = 'pres.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        '''
        connection = sqlite3.connect('order.db')
        cursor = connection.cursor()
        query = "INSERT INTO presorder VALUES (NULL, ?, ?, 0)"
        cursor.execute(query, (data['username'], data['pres']))
        connection.commit()
        connection.close()
        return True, 200



class LandmarkAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('landmark_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    parser.add_argument('landmark_type',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    parser.add_argument('latitude',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    parser.add_argument('longitude',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    #@jwt_required()
    def post(self):
        data = LandmarkAdd.parser.parse_args()
        '''
        connection = sqlite3.connect('order.db')
        cursor = connection.cursor()
        query = "INSERT INTO presorder VALUES (NULL, ?, ?, 0)"
        cursor.execute(query, (data['username'], data['pres']))
        connection.commit()
        connection.close()
        '''

        print(data)
        # connection = psycopg2.connect(user="postgres",
        #                               password="anuj@150100",
        #                               host="127.0.0.1",
        #                               port="5432",
        #                               database="MapifyDb")
        #
        # cursor = connection.cursor()
        #
        #
        # postgres_insert_query = """ INSERT INTO Landmark(Landmark_name, Landmark_type, Landmark_location) VALUES (%s,%s, Point(%s, %s))"""
        # record_to_insert = (data["landmarkName"], data["landmarkType"],[data["latitude"] ,data["longitude"] ])

        # cursor.execute(postgres_insert_query, record_to_insert)
        # connection.commit()


        return True, 200