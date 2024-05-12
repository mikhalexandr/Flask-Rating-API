from flask_restful import Resource, abort
from flask import jsonify, request

from data import db_session
from data.users import User


class DeleteResource(Resource):
    @staticmethod
    def delete():
        name = request.json["name"]
        password = request.json["password"]
        session = db_session.create_session()
        user: User = session.get(User, name)
        if user is None:
            abort(101, message=f"User {name} not found")
        if user.password != password:
            abort(102, message=f"User {name} password is incorrect")
        session.delete(user)
        session.commit()
        return jsonify({"success": "OK"})
