# -*- coding: utf-8 -*-

"""

    server.config.default
    ~~~~~~~~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


class DefaultConfig(object):

    DEBUG = 1

    SECURITY_REGISTERABLE = 1

    SECURITY_SEND_REGISTER_EMAIL = 0

    SECURITY_PASSWORD_HASH = "bcrypt"

    SECURITY_USER_IDENTITY_ATTRIBUTES = ("email", )  # https://github.com/mattupstate/flask-security/issues/124
    
    SQLALCHEMY_TRACK_MODIFICATIONS = 0

