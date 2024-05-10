from flask_restful import Resource, reqparse, abort
from sqlalchemy import desc
from flask import jsonify
from data import db_session
from data.users import User


class UserResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("password", required=True)
        parser.add_argument("level_amount", required=True)
        parser.add_argument("time", required=True)
        args = parser.parse_args()
        session = db_session.create_session()
        if session.query(User).filter(User.name == args["name"]).first() is not None:
            abort(400, message=f"User with name {args['name']} already exists")
        user = User(
            name=args["name"],
            password=args["password"],
            level_amount=args["level_amount"],
            time=args["time"],
        )
        session.add(user)
        session.commit()
        return jsonify({"success": "OK"})

    @staticmethod
    def put(user_name):
        parser = reqparse.RequestParser()
        parser.add_argument("level_amount")
        parser.add_argument("time")
        args = parser.parse_args()
        session = db_session.create_session()
        user: User = session.query(User).filter(User.name == user_name).first()
        if user is None:
            abort(404, message=f"User {user_name} not found")
        level_amount = args.get("level_amount")
        time = args.get("time")
        if level_amount:
            user.level_amount = level_amount
        if time:
            user.time = time
        session.commit()
        return jsonify({"success": "OK"})

    @staticmethod
    def get(user_name):
        session = db_session.create_session()
        user: User = session.query(User).filter(User.name == user_name).first()
        if user is None:
            abort(404, message=f"User {user_name} not found")
        return jsonify(
            {
                "name": user.name,
                "password": user.password,
                "level_amount": user.level_amount,
                "time": user.time,
            }
        )
