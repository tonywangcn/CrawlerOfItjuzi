# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	company_link = scrapy.Field()
	company_name = scrapy.Field()
	scope = scrapy.Field()
	subscope = scrapy.Field()
	prov = scrapy.Field()
	website = scrapy.Field()
	tag = scrapy.Field()
	description = scrapy.Field()
	full_name = scrapy.Field()
	regtime = scrapy.Field()
	invest_date = scrapy.Field()
	invest_round = scrapy.Field()
	financing_amount = scrapy.Field()
	investfirm = scrapy.Field()
	team = scrapy.Field()
	phone = scrapy.Field()
	email = scrapy.Field()
	address = scrapy.Field()
	follower = scrapy.Field()
	comment = scrapy.Field()
	pageview = scrapy.Field()
