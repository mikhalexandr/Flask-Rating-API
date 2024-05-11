import sqlalchemy

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String)
    level_amount = sqlalchemy.Column(sqlalchemy.Integer)
    time = sqlalchemy.Column(sqlalchemy.Integer)
