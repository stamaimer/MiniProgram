# -*- coding: utf-8 -*-

"""

    server.app.model.user
    ~~~~~~~~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


from flask_security import UserMixin

from . import db ,roles_users, AppModel


class User(AppModel, UserMixin):

    email = db.Column(db.String(255), nullable=0, unique=1)
    
    active = db.Column(db.Boolean, default=1)

    password = db.Column(db.String(255), nullable=0)

    roles = db.relationship("Role", secondary=roles_users,
                            backref=db.backref("users", lazy="dynamic"))

    def __init__(self, email='', active=1, password='', roles=[]):

        self.email = email
        
        self.active = active
        
        self.password = password
        
        self.roles = roles

    def __repr__(self):
        return self.email

