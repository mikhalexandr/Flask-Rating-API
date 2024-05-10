from flask_restful import Resource, abort
from flask import jsonify, request
from data import db_session
from data.users import User


class UserResource(Resource):
    @staticmethod
    def post():
        name = request.json["name"]
        password = request.json["password"]
        level_amount = request.json["level_amount"]
        time = request.json["time"]
        session = db_session.create_session()
        if session.query(User).filter(User.name == name).first() is not None:
            abort(400, message=f"User with name {name} already exists")
        user = User(
            name=name,
            password=password,
            level_amount=level_amount,
            time=time,
        )
        session.add(user)
        session.commit()
        return jsonify({"success": "OK"})

    @staticmethod
    def put(user_name):
        level_amount = request.json["level_amount"]
        time = request.json["time"]
        session = db_session.create_session()
        user: User = session.get(User, user_name)
        if user is None:
            abort(404, message=f"User {user_name} not found")
        if level_amount:
            user.level_amount = level_amount
        if time:
            user.time = time
        session.commit()
        return jsonify({"success": "OK"})
