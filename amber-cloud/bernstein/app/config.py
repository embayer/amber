# -*- coding: utf-8 -*-
__author__ = "Markus Bayer"
"""
configuration file
different modes are selected via the environment variable FLASK_CONFIG
"""

from os import path


class Config(object):
    DEBUG = False
    PORT = 5000
    HOST = "127.0.0.1"
    URL_PREFIX = "/api"
    PROJECT_ROOT = path.abspath(path.dirname(__file__))


class Development(Config):
    DEBUG = True
    SECRET_KEY = "development"


class Production(Config):
    pass


class Testing(Config):
    TESTING = True
    SECRET_KEY = "testing"
