# -*- coding: utf-8 -*-
__author__ = "Markus Bayer"
"""
initialization
"""


from flask import Flask
import os

from v1 import api_v1_bp, API_VERSION_V1
from v2 import api_v2_bp, API_VERSION_V2


def create_app(environment=None):
    """
    flask app factory
    does the app setup
    see: http://flask.pocoo.org/docs/0.10/patterns/appfactories/
    """
    app = Flask(__name__)

    # decide in which mode the app launches
    if not environment:
        # use FLASK_CONFIG environment variable or development if not set
        environment = os.environ.get("FLASK_CONFIG", "development")
    app.config.from_object("app.config.{}".format(environment.capitalize()))
    app.config.from_pyfile(
        "config_{}.py".format(environment.lower()),
        silent=True
        )

    # register the blueprints
    app.register_blueprint(
        api_v1_bp,
        url_prefix="{prefix}/v{version}".format(
            prefix=app.config["URL_PREFIX"],
            version=API_VERSION_V1))

    app.register_blueprint(
        api_v2_bp,
        url_prefix="{prefix}/v{version}".format(
            prefix=app.config["URL_PREFIX"],
            version=API_VERSION_V2))

    return app
