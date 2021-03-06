# -*- coding: utf-8 -*-

"""
    
    server.app
    ~~~~~~~~~~

    stamaimer 05/01/18

"""


from werkzeug import import_string

import flask


extensions = [
    "app.model:db",
#    "app.admin.admin",
#    "app.extensions.session.session",
    "app.extensions.security:security"
]

blueprints = [
    "app.api.api",
    "app.main.main"
]


def create_app(config_name):

    app = flask.Flask(__name__, instance_relative_config=1)

    app.config.from_object(config_name)
    app.config.from_pyfile("config.py")

    for name in extensions:
        extension = import_string(name)
        extension.init_app(app)

    for name in blueprints:
        blueprint = import_string(name)
        app.register_blueprint(blueprint)

    return app

