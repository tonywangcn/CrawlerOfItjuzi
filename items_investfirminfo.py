# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	firm_link = scrapy.Field()
	firm_site = scrapy.Field()
	firm_info = scrapy.Field()
	investment_field = scrapy.Field()
	investment_round = scrapy.Field()
	investment_cube = scrapy.Field()
	incumbent_emp = scrapy.Field()
	ex_emp = scrapy.Field()
