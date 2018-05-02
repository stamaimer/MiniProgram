# -*- coding: utf-8 -*-

"""

    server.app.api
    ~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


import flask

from app.model import db
from app.extensions.security import user_datastore


api = flask.Blueprint("api", __name__, url_prefix="/api")


@api.before_app_first_request
def init_db():

    db.create_all()

    user_datastore.create_user(email="test@example.com", password="test")

    db.session.commit()

