# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	investor_link = scrapy.Field()
	investor_name = scrapy.Field()
	address = scrapy.Field()
	investment_stage = scrapy.Field()
	investment_field = scrapy.Field()
	investor_info = scrapy.Field()
	investcase = scrapy.Field()
	work_experience = scrapy.Field()
	educational_experience = scrapy.Field()
	service_organization = scrapy.Field()
