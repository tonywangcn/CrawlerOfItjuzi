# -*- coding: utf-8 -*-
import scrapy

from scrapy.loader import ItemLoader
from itjuzi.items import ItjuziItem

class InvestorlinksSpider(scrapy.Spider):
    name = "investorlinks"
    allowed_domains = ["https://www.itjuzi.com"]
    start_urls = (
        'https://www.itjuzi.com/investor?page=%d'%n for n in range(1,244)
    )

    def parse(self, response):
        l = ItemLoader(item = ItjuziItem(),response=response)
	l.add_xpath('website',"//b[@class='title']//@href")
	print l
	return l.load_item()

