# -*- coding: utf-8 -*-

"""

    server.manage
    ~~~~~~~~~~~~~

    stamaimer 05/01/18

"""


from flask_script import Manager

from app import create_app


app = create_app("config.DefaultConfig")

manager = Manager(app)


if __name__ == "__main__":
    manager.run()

