# -*- coding: utf-8 -*-

"""

    server.run
    ~~~~~~~~~~

    stamaimer 05/01/18

"""


from app import create_app


app = create_app("config.DefaultConfig")


if __name__ == "__main__":

    app.run()
