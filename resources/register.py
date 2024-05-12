from flask_restful import Resource, abort
from flask import jsonify, request

from data import db_session
from data.users import User


class RegisterResource(Resource):
    @staticmethod
    def post():
        name = request.json["name"]
        password = request.json["password"]
        level_amount = request.json["level_amount"]
        time = request.json["time"]
        session = db_session.create_session()
        if session.query(User).filter(User.name == name).first() is not None:
            abort(100, message=f"User with name {name} already exists")
        user = User(
            name=name,
            level_amount=level_amount,
            time=time,
        )
        user.set_password(password)
        session.add(user)
        session.commit()
        return jsonify({"success": "OK"})
