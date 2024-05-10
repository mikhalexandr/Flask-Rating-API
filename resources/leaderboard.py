from flask_restful import Resource
from flask import jsonify
from data import db_session
from data.users import User


class LeaderboardResource(Resource):
    @staticmethod
    def get():
        pass
