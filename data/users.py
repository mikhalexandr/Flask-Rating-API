import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    level_amount = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    time = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
