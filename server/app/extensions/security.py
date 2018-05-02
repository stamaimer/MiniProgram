# -*- coding: utf-8 -*-

"""

    server.app.extensions.security
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


from flask_security import Security, SQLAlchemyUserDatastore

from app.model import db, Role, User


user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(datastore=user_datastore)

