from flask_restful import Resource, abort
from flask import jsonify, request

from data import db_session
from data.users import User


class UpdateRecordResource(Resource):
    @staticmethod
    def patch():
        name = request.json["name"]
        level_amount = request.json["level_amount"]
        time = request.json["time"]
        session = db_session.create_session()
        user: User = session.get(User, name)
        if user is None:
            abort(404, message=f"User [{name}] is not found")
        if level_amount:
            user.level_amount = level_amount
        if time:
            user.time = time
        session.commit()
        return jsonify({"message": "OK"})


class UpdateNameResource(Resource):
    @staticmethod
    def patch():
        name = request.json["name"]
        new_name = request.json["new_name"]
        password = request.json["password"]
        session = db_session.create_session()
        user: User = session.get(User, name)
        if user is None:
            abort(404, message=f"User [{name}] is not found")
        if not user.check_password(password):
            abort(401, message=f"[{name}]'s user password is incorrect")
        if session.get(User, new_name) is not None:
            abort(409, message=f"User [{new_name}] already exists")
        user.name = new_name
        session.commit()
        return jsonify({"message": "OK"})


class UpdatePasswordResource(Resource):
    @staticmethod
    def patch():
        name = request.json["name"]
        password = request.json["password"]
        new_password = request.json["new_password"]
        session = db_session.create_session()
        user: User = session.get(User, name)
        if user is None:
            abort(404, message=f"User [{name}] is not found")
        if not user.check_password(password):
            abort(401, message=f"[{name}]'s user password is incorrect")
        if user.check_password(new_password):
            abort(409, message=f"[{name}]'s user password is the same as the old one")
        user.set_password(new_password)
        session.commit()
        return jsonify({"message": "OK"})
