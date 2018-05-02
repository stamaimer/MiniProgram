# -*- coding: utf-8 -*-

"""

    server.app.model.role
    ~~~~~~~~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


from flask_security import RoleMixin

from . import db, AppModel


class Role(AppModel, RoleMixin):

    name = db.Column(db.String(64), nullable=0, unique=1)

    description = db.Column(db.Text())

    def __init__(self, name='', description=''):

        self.name = name
        
        self.description = description

    def __repr__(self):
        return self.name

