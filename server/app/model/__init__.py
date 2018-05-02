# -*- coding: utf-8 -*-

"""

    server.app.model
    ~~~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


from sqlalchemy import func

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class AppModel(db.Model):

    __abstract__ = 1

    id = db.Column(db.Integer, primary_key=1)

    create_datetime = db.Column(db.DateTime, default=func.now())

    update_datetime = db.Column(db.DateTime, default=func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        pass


roles_users = db.Table("roles_users",
                       db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
                       db.Column("user_id", db.Integer, db.ForeignKey("user.id")))

from .role import Role
from .user import User

