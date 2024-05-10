from flask_restful import Resource
from operator import itemgetter
from flask import jsonify
from data import db_session
from data.users import User


class LeaderboardResource(Resource):
    @staticmethod
    def get(user_name):
        session = db_session.create_session()
        users = session.query(User).all()
        leaders = []
        for user in users:
            leaders.append(
                    {
                        "name": user.name,
                        "level_amount": user.level_amount,
                        "time": user.time,
                    }
            )
        sorted_leaders = sorted(leaders, key=itemgetter("level_amount", "time"), reverse=True)
        user_index = [user["name"] for user in sorted_leaders].index(user_name)
        result = [leaders[:10], leaders[user_index]]
        return jsonify(result)
