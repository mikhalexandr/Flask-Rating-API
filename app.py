import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from data import db_session
from resources import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False


def add_resources():
    api = Api(app)
    api.add_resource(LeaderboardResource, "/api/leaderboard/<user_name>")
    api.add_resource(UserAddResource, "/api/user/add")
    api.add_resource(UserUploadResource, "/api/user/upload/<user_name>")


def main():
    if not os.path.isdir("db"):
        os.mkdir("db")
    db_session.global_init("db/Users.db")
    add_resources()
    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    main()
