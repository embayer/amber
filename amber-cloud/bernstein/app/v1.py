# -*- coding: utf-8 -*-
__author__ = "Markus Bayer"
"""
Resources for the bernstein api v1
"""


from flask import Blueprint
from flask_restful import Api, Resource


API_VERSION_V1 = 1.0
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint("api_v1", __name__)
api_v1 = Api(api_v1_bp)


class HelloWorld(Resource):
    def get(self):
        return {
            "hello": "world",
            "version": API_VERSION,
            }


api_v1.add_resource(HelloWorld, "/helloworld")
