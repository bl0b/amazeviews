# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class AmazeviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Review(scrapy.Item):
    author_name = scrapy.Field()
    author_url = scrapy.Field()
    rating = scrapy.Field()
    amz_id = scrapy.Field()
    text = scrapy.Field()
    tld = scrapy.Field()
    book_id=scrapy.Field()


class ReviewLoader(ItemLoader):
    default_output_processor = TakeFirst()
