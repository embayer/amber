# -*- coding: utf-8 -*-
__author__ = "Markus Bayer"
"""
connector for mongodb
"""

from pymongo import MongoClient


# docker uri
# mongo_app = MongoClient("mongodb://storage:27017")
# regular uri
mongo_app = MongoClient("mongodb://localhost:27017")

metacart_db = mongo_app["metacart"]
