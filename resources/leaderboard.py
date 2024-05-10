from flask_restful import Resource
from flask import jsonify
from data import db_session
from data.users import User


class LeaderboardResource(Resource):
    @staticmethod
    def get():
        session = db_session.create_session()
        users = session.query(User).filter(User.id < 11).all()
        result = []
        for user in users:
            result.append(
                    {
                        "id": user.id,
                        "name": user.name,
                        "level_amount": user.level_amount,
                        "time": user.time,
                    }
            )
        return jsonify(result)
