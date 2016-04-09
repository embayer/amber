# -*- coding: utf-8 -*-

#  Creation Date: 07.04.2015


from __future__ import absolute_import

from kumpel.celeryapp import app
from kumpel.mongoapp import mongo_app, metacart_db
from kumpel.network.ikea import Ikea


@app.task(ignore_result=True)
def test_task(x, y):
    res = x + y
    print res

    return res


@app.task(ignore_result=True)
def fetch_ikea_product(prod_url):
    ikea = Ikea(prod_url)
    doc = ikea.fetch_product()

    # check if new
    stored_doc = ""
    cursor = metacart_db.product.find({"name": doc["name"]})
    if cursor.count() == 0:
        stored_doc = metacart_db.product.insert_one(doc)

    if stored_doc:
        print "stored new documet: %s" % stored_doc.inserted_id


@app.task(ignore_result=True)
def store_product(product):
    pass
