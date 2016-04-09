# -*- coding: utf-8 -*-

#  Creation Date: 03.05.2015

from __future__ import absolute_import

from pymongo import MongoClient


mongo_app = MongoClient("mongodb://storage:27017")

metacart_db = mongo_app["metacart"]
