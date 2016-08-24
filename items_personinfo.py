# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	person_link = scrapy.Field()
	person_name = scrapy.Field()
	address = scrapy.Field()
	person_info = scrapy.Field()
	enterprise_experience = scrapy.Field()
	work_experience = scrapy.Field()
	educational_experience = scrapy.Field()
