# -*- coding: utf-8 -*-

"""

    server.app.main
    ~~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""

import flask

from flask_security import login_required


main = flask.Blueprint("main", __name__)


@main.route('/')
@login_required
def index():
    return "Hello, MiniProgram!"

