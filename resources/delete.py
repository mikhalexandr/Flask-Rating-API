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
            abort(404, message=f"User [{name}] is not found")
        if not user.check_password(password):
            abort(401, message=f"[{name}]'s user password is incorrect")
        session.delete(user)
        session.commit()
        return jsonify({"message": "OK"})
