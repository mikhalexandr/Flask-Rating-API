from flask_restful import Resource
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
        sorted_leaders = sorted(leaders, key=lambda x: (-x["level_amount"], x["time"]))
        user_index = [x for x in range(len(sorted_leaders)) if sorted_leaders[x]["name"] == user_name][0]
        result = [sorted_leaders[:10], user_index + 1]
        return jsonify(result)
