# -*- coding: utf-8 -*-

#  Creation Date: 02.05.2015

from __future__ import absolute_import

from urllib2 import urlopen
from lxml import etree
import re


class Ikea(object):
    # API_URL = "http://www.ikea.com/de/de/catalog/products/80263832/?type=xml&amp;dataset=normal,allImages,prices,attributes"
    API_BASE_URL = "http://www.ikea.com/"
    API_PARAMS = "?type=xml&amp;dataset=normal,allImages,prices,attributes"

    def __init__(self, prod_url):
        self.prod_url = prod_url
        self.prod_id = self.extract_prod_id(self.prod_url)

    def extract_prod_id(self, prod_url):
        return prod_url.split("/")[-2]

    def extract_country(self, prod_url):
        return prod_url.split("/")[3]

    def extract_lang(self, prod_url):
        return prod_url.split("/")[4]

    def build_request(self):
        country = self.extract_country(self.prod_url)
        lang = self.extract_lang(self.prod_url)
        req = "%s%s/%s/catalog/products/%s/%s" % (self.API_BASE_URL, country, lang, self.prod_id, self.API_PARAMS)

        return req

    def request(self, req):
        return urlopen(req).read()

    def extract_product(self, xml):
        pass

    def fetch_product(self):
        product = {"product_id": self.prod_id}

        req = self.build_request()
        xml = self.request(req)

        xml = etree.fromstring(xml)

        el_item = xml.xpath("products/product/items/item")[0]

        p_name = el_item.findtext(".//name")
        p_name_suffix = el_item.findtext(".//facts")

        product["name"] = "%s (%s)" % (p_name, p_name_suffix)

        p_description = el_item.findtext(".//custBenefit")
        # remove tags
        product["description"] = re.sub('<[^>]*>', '', p_description)
        product["image"] = el_item.xpath("images/normal/image")[0].text
        product["price"] = el_item.xpath("prices/normal/priceNormal")[0].text

        print "product_id: %s" % product["product_id"]
        print "name: %s" % product["name"]
        print "description: %s" % product["description"]
        print "price: %s" % product["price"]
        print "image: %s" % product["image"]
        print "-----------------------------------------------------------------------------------------------------------------------"

        return product
