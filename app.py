import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from data import db_session
from resources import *


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def check_work():
    return "OK"


def add_resources():
    api = Api(app)
    api.add_resource(RegisterResource, "/api/register")
    api.add_resource(LoginResource, "/api/login")
    api.add_resource(UpdateNameResource, "/api/update/name")
    api.add_resource(UpdatePasswordResource, "/api/update/password")
    api.add_resource(UpdateRecordResource, "/api/update/record")
    api.add_resource(DeleteResource, "/api/delete")
    api.add_resource(RatingResource, "/api/rating")


def main():
    if not os.path.isdir("db"):
        os.mkdir("db")
    db_session.global_init("db/Users.db")
    add_resources()
    app.run()


if __name__ == "__main__":
    main()

