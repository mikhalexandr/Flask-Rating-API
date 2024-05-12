from flask_restful import Resource, abort
from flask import jsonify, request

from data import db_session
from data.users import User


class RegisterResource(Resource):
    @staticmethod
    def post():
        name = request.json["name"]
        password = request.json["password"]
        session = db_session.create_session()
        if session.query(User).filter(User.name == name).first() is not None:
            abort(409, message=f"User with name [{name}] already exists")
        user = User(
            name=name,
        )
        user.set_password(password)
        session.add(user)
        session.commit()
        return jsonify({"message": "OK"})
