# -*- coding: utf-8 -*-
__author__ = "Markus Bayer"
"""
Resources for the bernstein api v2
"""


from flask import Blueprint
from flask_restful import Api, Resource


API_VERSION_V2 = 2.0
API_VERSION = API_VERSION_V2

api_v2_bp = Blueprint("api_v2", __name__)
api_v2 = Api(api_v2_bp)


class HelloWorld(Resource):
    def get(self):
        return {
            "HELLO": "WORLD",
            "VERSION": API_VERSION,
            }


api_v2.add_resource(HelloWorld, "/helloworld")
