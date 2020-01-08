# -*- coding: utf-8 -*-
import scrapy

class ScrapexmlItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    desc = scrapy.Field()
    # define the fields for your item here like:
    pass
