# -*- coding: utf-8 -*-
__author__ = "Markus Bayer"
"""
starting point to run the flask server
"""


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"])
