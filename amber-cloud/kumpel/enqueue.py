# -*- coding: utf-8 -*-

#  Creation Date: 07.04.2015

from __future__ import absolute_import

from kumpel.tasks import test_task
from kumpel.tasks import fetch_ikea_product
from kumpel.celeryapp import app

# app.control.purge()
def test_queue():
    for i in range(0, 9):
        test_task.apply_async(args=[2, 2], queue="default", routing_key="default")

def add_ikea_product():
    prod_urls = [
            "http://www.ikea.com/de/de/catalog/products/80263832/",
            "http://www.ikea.com/de/de/catalog/products/50268831/",
            "http://www.ikea.com/de/de/catalog/products/30261270/",
            "http://www.ikea.com/de/de/catalog/products/20119461/",
            "http://www.ikea.com/de/de/catalog/products/80193231/",
            "http://www.ikea.com/de/de/catalog/products/10193239/",
            "http://www.ikea.com/de/de/catalog/products/90186094/"
            ]

    for prod_url in prod_urls:
        fetch_ikea_product.apply_async(args=[prod_url], queue="fetch_ikea_q", routing_key="media.fetch")
